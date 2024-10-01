import boto3
import json
import logging
from botocore.exceptions import ClientError

# Set the correct model ID for Llama 3.
MODEL_ID = "meta.llama3-70b-instruct-v1:0"  # Ensure this is the correct model ID
REGION = "us-west-2"  # Specify the correct region

def analyze_and_correct_code():
    try:
        # Read the code from the file
        logging.info("Original code loaded for review.")
        with open('src/handlers/EventHandler.py', 'r') as file:
            code = file.read()

        # Correct the code with Llama 3 via Bedrock
        corrected_code = correct_code_with_llama3(code)

        if corrected_code and corrected_code != code:
            # Write the corrected code to the same file
            with open('src/handlers/EventHandler.py', 'w') as file:
                file.write(corrected_code)
            logging.info("Corrected code written back to the file.")
        else:
            logging.info("No corrections were made.")

    except Exception as e:
        logging.error(f"Error during code review: {str(e)}")
        exit(1)

def correct_code_with_llama3(code):
    # Create a Bedrock Runtime client
    client = boto3.client("bedrock-runtime", region_name=REGION)

    # Prepare the prompt for Llama 3
    logging.info("Sending code to Llama 3 for analysis.")
    prompt = f"Review the following Python code for errors and provide corrections:\n\n{code}\n\nProvide the corrected code below:\n"
    
    # Format the request payload
    formatted_prompt = f"""
    <|begin_of_text|><|start_header_id|>user<|end_header_id|>
    {prompt}
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """

    native_request = {
        "prompt": formatted_prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
    }

    # Send the request to Llama 3
    try:
        request = json.dumps(native_request)
        response = client.invoke_model(modelId=MODEL_ID, body=request)
        model_response = json.loads(response["body"].read())

        # Extract the generated corrected code from the response
        corrected_code = model_response["generation"]
        logging.info("Received corrected code from Llama 3.")
        return corrected_code

    except (ClientError, Exception) as e:
        logging.error(f"Failed to retrieve corrected code from Llama 3: {e}")
        return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    analyze_and_correct_code()


