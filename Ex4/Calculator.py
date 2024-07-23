#Assignment 4: Defining Functions in Python
#1. Create a new Python file named `calculator.py`.
#2. Define a function named `add` that takes two arguments and returns their sum.
def add(num1, num2) :
    return num1 + num2
#3. Define a function named `subtract` that takes two arguments and returns their difference.
def subtract(num1, num2) :
    return num1 - num2
#4. Define a function named `multiply` that takes two arguments and returns their product.
def multiply(num1, num2) :
    return num1 * num2
#5. Define a function named `divide` that takes two arguments and returns their quotient.
def divide(num1, num2) :
    return num1 / num2
#6. Write a main block that calls each function with sample inputs and prints the results.
print(f"Add function = {add(14, 4)}")
print(f"Subtract function = {subtract(14, 4)}")
print(f"Multiply function = {multiply(14, 4)}")
print(f"Divide function = {divide(14, 2)}")