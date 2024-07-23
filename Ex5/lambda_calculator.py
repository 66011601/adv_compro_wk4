#Assignment 5: Using Lambda Functions in Python
#1. Create a new Python file named `lambda_calculator.py`.
#2. Define a lambda function for addition that takes two arguments and returns their sum.
Addition = lambda num1, num2: num1+num2
#3. Define a lambda function for subtraction that takes two arguments and returns their difference.
Subtraction = lambda num1, num2: num1-num2
#4. Define a lambda function for multiplication that takes two arguments and returns their product.
Multiplication = lambda num1, num2: num1*num2
#5. Define a lambda function for division that takes two arguments and returns their quotient.
Division = lambda num1, num2: num1/num2
#6. Write a main block that calls each lambda function with sample inputs and prints the results.
num1 = 24
num2 = 6
print(f"Add function = {Addition(num1, num2)}")
print(f"Subtract function = {Subtraction(num1, num2)}")
print(f"Multiply function = {Multiplication(num1, num2)}")
print(f"Divide function = {Division(num1, num2)}")