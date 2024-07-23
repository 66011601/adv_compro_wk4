#Assignment 6: Importing Modules in Python
#1. Create a new Python file named `string_operations.py`.
#2. Define functions for common string operations:
"""    
    - `reverse_string`: Reverses a given string.
    - `capitalize_string`: Capitalizes the first letter of a given string.
    - `lowercase_string`: Converts all characters in a given string to lowercase.
    - `uppercase_string`: Converts all characters in a given string to uppercase. 
"""
#3. Create another Python file named `main.py`. 
#4. Import the `string_operations` module in `main.py`.
import string_operations as string
#5. Use the imported functions to perform operations on sample strings and print the results.

# Sample strings and printing results using string_operations.py
sample_string = "hello World"
print("Original:", sample_string)
print(f"Reverse String : {string.reverse_string(sample_string)}")
print(f"Capitalize First letter : {string.capitalize_string(sample_string)}")
print(f"Lowercase String : {string.lowercase_string(sample_string)}")
print(f"Uppercase String : {string.uppercase_string(sample_string)}")