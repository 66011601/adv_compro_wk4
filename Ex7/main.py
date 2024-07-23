#Assignment 7: Creating Packages in Python
#1. Create a directory named `utilities`.
#2. Inside `utilities`, create an `__init__.py` file.
#3. Create a module named `calculator.py` inside `utilities` and include the functions defined in Assignment 4.
#5. Create a module named `string_operations.py` inside `utilities` and include the functions defined in Assignment 6.
#6. Create another Python file named `main.py` outside the `utilities` directory.
#7. Import functions from all three modules (`calculator` and `string_operations`) in `main.py`.
from utilities import calculator as c 
from utilities import string_operations as s 
#8. Use the imported functions to perform operations and print the results.

# Sample inputs and printing results using calculator.py
print("Using calculator.py:")
print(f"Add function = {c.add(14, 4)}")
print(f"Subtract function = {c.subtract(14, 4)}")
print(f"Multiply function = {c.multiply(14, 4)}")
print(f"Divide function = {c.divide(14, 2)}")

# Sample strings and printing results using string_operations.py
sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print(f"Reverse String : {s.reverse_string(sample_string)}")
print(f"Capitalize First letter : {s.capitalize_string(sample_string)}")
print(f"Lowercase String : {s.lowercase_string(sample_string)}")
print(f"Uppercase String : {s.uppercase_string(sample_string)}")