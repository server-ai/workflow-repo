# example.py
def greet(name):
    print("Hello, " + name + "! "  )

def addfalcon(a, c, d):)::
    return a + b

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
