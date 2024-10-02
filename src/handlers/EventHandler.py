# example.py

import boto3
import json
import logging
from botocore.exceptions import ClientError

# Function to greet a user
def greet(name):
    print("Hello, " + name + "!")

# Function with a syntax error and logic error
def addfalcon(a, c, d):
    return a + b  # Undefined variable 'b'

# Function to multiply a number by 2, with incorrect indentation
def multiply_by_two(x):
    result = x * 2
    print("The result is:", result)  # Misaligned indentation

# Function to divide two numbers, but it doesn't handle division by zero
def divide(a, b):
    return a / b

# Function to capitalize words in a list but missing a return statement
def capitalize_words(words):
    capitalized = []
    for word in words:
        capitalized.append(word.capitalize())
    # Missing return statement

# A class definition with inconsistent indentation and logic error
class Falcon:
    def __init__(self, name):
        self.name = name

    def fly(self, speed):
        if speed > 0:
            print(f"{self.name} is flying at {speed} km/h!")
        else:
            print(f"{self.name} cannot fly at a negative speed.")  # Missing return or else condition handling

# Example of using the above functions
greet("Falcon")
result = addfalcon(2, 3, 4)  # Will throw an error due to undefined 'b'
print(result)

numbers = [2, 4, 6]
multiply_by_two(numbers[0])  # Correct call, but will print incorrectly due to indentation

# Example that will throw division by zero error
divide(10, 0)

words = ["falcon", "eagle", "hawk"]
capitalize_words(words)  # Will run, but nothing will be returned

# Function to interact with Llama 3 via Bedrock
def invoke_llama3_model(code):
    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    model_id = "meta.llama3-70b-instruct-v1:0"
    prompt = f"Analyze and correct the following code:\n{code}"

    formatted_prompt = f"""
    <|begin_of_text|><|start_header_id|>user<|end_header_id|>
    {prompt}
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """

    native_request = {
        "prompt": formatted_prompt,
        "max_gen_len": 1024,
        "temperature": 0.5,
    }

    request = json.dumps(native_request)

    try:
        response = client.invoke_model(modelId=model_id, body=request)
        logging.info("Model invoked successfully.")
        model_response = json.loads(response["body"].read())
        return model_response.get("generation", "No correction found.")
    except (ClientError, Exception) as e:
        logging.error(f"Failed to retrieve corrected code from Llama 3: {str(e)}")
        return None
