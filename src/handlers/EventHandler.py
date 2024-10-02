 Here is the corrected Python code:

```python
# example.py

# Function to greet a user
def greet(name):
    print("Hello, " + name + "! ")

# Function to add three numbers
def addfalcon(a, b, c):
    return a + b + c

# Function to multiply a number by 2
def multiply_by_two(x):
    result = x * 2
    print("The result is:", result)

# Function to divide two numbers, handling division by zero
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    else:
        return a / b

# Function to capitalize words in a list
def capitalize_words(words):
    capitalized = []
    for word in words:
        capitalized.append(word.capitalize())
    return capitalized

# A class definition with consistent indentation and logic error fixed
class Falcon:
    def __init__(self, name):
        self.name = name

    def fly(self, speed):
        if speed > 0:
            print(f"{self.name} is flying at {speed} km/h!")
            return True
        else:
            print(f"{self.name} cannot fly at a negative speed.")
            return False

# Example of using the above functions
greet("Falcon")
result = addfalcon(2, 3, 4)
print(result)

numbers = [2, 4, 6]
multiply_by_two(numbers[0])

# Example that will handle division by zero error
print(divide(10, 0))

words = ["falcon", "eagle", "hawk"]
print(capitalize_words(words))
```

Changes made:

1. Fixed syntax error in `addfalcon` function by removing extra colon at the end of the function definition.
2. Fixed logic error in `addfalcon` function by adding `b` to the return statement.
3. Fixed indentation error in `multiply_by_two` function by aligning the `print` statement.
4. Added error handling to `divide` function to prevent division by zero.
5. Added a `return` statement to `capitalize_words` function.
6. Fixed indentation and logic errors in `Falcon` class definition.
7. Fixed the `fly` method in `Falcon` class to return a boolean value indicating whether the falcon can fly or not.
8. Updated the example usage to reflect the corrected functions.