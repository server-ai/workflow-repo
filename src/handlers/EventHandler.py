# example_extended.py

# Function with a missing import and typo in variable usage
def fetch_data(url):
    response = requests.get(url)  # Missing import for requests module
    if response.stauts_code == 200:  # Typo in 'status_code'
        return response.json()
    else:
        return None

# Function with inconsistent indentation and a logical error
def process_data(data):
    result = []
    for item in data:
        if 'value' in item:
          result.append(item['value'] * 2)  # Inconsistent indentation
            result.append(item['value'] * 3)  # Logically incorrect line
    return result

# Function with an off-by-one error and undefined variable
def find_max(numbers):
    max_num = None
    for i in range(len(numbers)):
        if i == 0 or numbers[i] > max_num:
            max_num = numbers[i]
    return max_nu  # Typo, should be 'max_num'

# Function with a missing argument and wrong data type usage
def concatenate_strings(a, b, separator):
    return a + separator +  # Missing 'b' argument

# Function that divides by zero when given an empty list
def average(numbers):
    total = sum(numbers)
    return total / len(numbers)  # Will raise ZeroDivisionError if the list is empty

# Function that attempts to read a file without opening it
def read_file(file_path):
    file_data = file.read()  # Missing 'open' and context manager for 'file'
    return file_data
