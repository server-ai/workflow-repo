import boto3
import json
import logging
import os
from botocore.exceptions import ClientError

# Constants for AWS Bedrock
MODEL_ID = "meta.llama3-70b-instruct-v1:0"
REGION = "us-east-1"
CODEGURU_RESULTS_PATH = "C:\\Users\\d.lulkowski\\workflow-repo\\codeguru_results.json"  # Path to CodeGuru results
JAVA_FILE_PATH = "C:\\Users\\d.lulkowski\\workflow-repo\\src\\handlers\\EventHandler.java"  # Path to the Java file

def analyze_and_correct_code():
    try:
        # Load the CodeGuru recommendations from the JSON file
        logging.info("Loading CodeGuru recommendations...")
        json_file_path = os.path.abspath(CODEGURU_RESULTS_PATH)
        logging.info(f"JSON file path: {json_file_path}")

        with open(json_file_path, 'r') as file:
            content = file.read()
            logging.info(f"Content length of the JSON file: {len(content)}")  # Check content length
            
            if not content.strip():  # Check if content is empty
                logging.error("The JSON file is empty. Please check the file content.")
                return  # Exit or handle appropriately
            
            logging.info(f"Content of the JSON file: {content}")  # Log the content
            recommendations = json.loads(content)  # Load recommendations from JSON

        logging.info(f"Recommendations loaded: {json.dumps(recommendations, indent=2)}")

        # Open the original Java code file
        logging.info(f"Loading original code from {JAVA_FILE_PATH}...")
        with open(JAVA_FILE_PATH, 'r') as code_file:
            code = code_file.read()

        logging.info("Original code loaded for review.")

        # Send code and CodeGuru recommendations to LLaMA 3 via Bedrock
        corrected_code = correct_code_with_llama3(code, recommendations)
        
        if corrected_code and corrected_code != code:
            # Write the corrected code back to the file
            with open(JAVA_FILE_PATH, 'w') as code_file:
                code_file.write(corrected_code)
            logging.info("Corrected code written back to the file.")
        else:
            logging.info("No corrections were made.")
            
    except Exception as e:
        logging.error(f"Error during code review: {str(e)}")
        logging.exception("Exception caught:")
        exit(1)

def correct_code_with_llama3(code, recommendations):
    client = boto3.client("bedrock-runtime", region_name=REGION)

    # Prepare the prompt for LLaMA 3
    logging.info("Sending code and CodeGuru recommendations to LLaMA 3 for corrections.")
    prompt = (
        "Here is the original code:\n\n"
        f"{code}\n\n"
        "Please apply the following CodeGuru recommendations:\n"
        f"{json.dumps(recommendations, indent=2)}\n\n"
        "Ensure that the corrected code compiles without errors."
    )
    
    native_request = {
        "prompt": prompt,
        "max_gen_len": 1024,
        "temperature": 0.7
    }

    try:
        request = json.dumps(native_request)
        response = client.invoke_model(modelId=MODEL_ID, contentType='application/json', body=request)
        model_response = json.loads(response['body'].read())

        corrected_code = model_response.get("generation", "")
        logging.info("Received corrected code from LLaMA 3.")
        return corrected_code

    except ClientError as e:
        logging.error(f"ClientError: Failed to retrieve corrected code from LLaMA 3: {e}")
        return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    analyze_and_correct_code()
