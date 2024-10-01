import boto3
import logging
import json

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Constants for AWS Bedrock
MODEL_ID = "meta-llama-3"  # Assuming this is the correct model ID, check AWS documentation
BEDROCK_ENDPOINT = "bedrock.us-east-1.amazonaws.com"  # Adjust this according to your AWS region

def analyze_and_correct_code():
    try:
        # Load the code from the file
        with open('src/handlers/EventHandler.py', 'r') as file:
            code = file.read()
        
        logging.info("Original code loaded for review.")
        
        # Get the corrected code using Llama 3
        corrected_code = correct_code_with_llama3(code)
        
        if corrected_code:
            # Write the corrected code back to the file
            with open('src/handlers/EventHandler.py', 'w') as file:
                file.write(corrected_code)
            logging.info("Corrected code written back to the file.")
        else:
            logging.info("No corrections were made.")

    except Exception as e:
        logging.error(f"Error during code review: {str(e)}")
        exit(1)

def correct_code_with_llama3(code):
    try:
        # Initialize the Bedrock client
        client = boto3.client('bedrock-runtime', region_name='us-east-1')
        
        # Define the input for Llama 3 model
        input_payload = {
            "inputText": code
        }
        
        logging.info("Sending code to Llama 3 for analysis.")
        
        # Call the Llama 3 model via Bedrock
        response = client.invoke_model(
            modelId=MODEL_ID,
            contentType='application/json',
            body=json.dumps(input_payload)
        )
        
        # Extract the corrected code from the response
        result = json.loads(response['body'])
        corrected_code = result.get('results', [{}])[0].get('outputText', '')
        
        if corrected_code:
            logging.info("Received corrected code from Llama 3.")
        else:
            logging.warning("No corrections were suggested by Llama 3.")
        
        return corrected_code

    except Exception as e:
        logging.error(f"Failed to retrieve corrected code from Llama 3: {str(e)}")
        return None

if __name__ == "__main__":
    analyze_and_correct_code()


