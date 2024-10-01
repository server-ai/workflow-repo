import boto3
import logging
import json

def analyze_and_correct_code():
    # Set up logging to capture the code analysis process
    logging.basicConfig(level=logging.INFO)
    
    try:
        # Load the Python code for analysis
        with open('src/handlers/EventHandler.py', 'r') as file:
            code = file.read()
            logging.info("Original code loaded for review.")

        # Call AWS Bedrock (Llama 3) for code analysis and corrections
        corrected_code = correct_code_with_llama3(code)

        # Write the corrected code back to the file or create a new file
        with open('src/handlers/EventHandler.py', 'w') as file:
            file.write(corrected_code)
            logging.info("Corrected code written back to the file.")

    except Exception as e:
        logging.error(f"Error during code review: {str(e)}")
        exit(1)


def correct_code_with_llama3(code):
    """
    Use AWS Bedrock's Llama 3 model to analyze and correct the given code.
    """

    try:
        # Create Bedrock client (Ensure boto3 is configured with the correct IAM permissions)
        client = boto3.client('bedrock', region_name='us-east-1')

        # Prepare the payload with code input for the model
        payload = {
            'modelInput': code, 
            'modelType': 'code-review',  # Example field, replace based on Bedrock's API docs
            'modelId': 'llama3'          # Specify the correct model name
        }

        # Invoke the Llama 3 model for code correction (adjust params as needed)
        response = client.invoke_model(
            ModelId='llama3',            # Replace with your actual model identifier
            ContentType='application/json',
            Payload=json.dumps(payload)  # Send the code as input in JSON format
        )

        # Extract the corrected code from the response
        response_body = response['Payload'].read()
        result = json.loads(response_body)

        # Assuming the API returns the corrected code under 'corrected_code' key
        corrected_code = result.get('corrected_code', code)
        logging.info("Code corrections received from Llama 3.")

        return corrected_code

    except Exception as e:
        logging.error(f"Failed to retrieve corrected code from Llama 3: {str(e)}")
        return code  # Return original code in case of failure


if __name__ == "__main__":
    analyze_and_correct_code()

