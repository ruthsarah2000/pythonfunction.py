'''
2. The Calculator App
Objective:
The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

Task 1: Create functions for each arithmetic operation.
Task 2: Implement user input to receive numbers and an operation choice.
Task 3: Ensure your program can handle division by zero and other potential errors.
'''
import math

def add (a, b):
    return a + b
def subtract (a, b):
    return a - b
def multiply (a, b):
    return a * b 
def divide (a, b):
    return a / b
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def user_numb():
    try:
        number_1 = float(int(input("Enter first number: ")))
        number_2 = float(int(input("Enter second number: ")))
        return number_1, number_2
    except ValueError:
        ("Cannot divide by zero")
        return user_numb()
def user_ops():
    operation = input("Enter the operation (+, -, *, /): ")
    if operation not in ['+', '-', '*', '/' ]:
        print("Invalid operation, please type one +, -, *, / to proceed.")
        return user_ops()
    return operation

def calculator():
    while True:
        try:
            number_1, number_2 = user_numb()
            operation = user_ops()
            if operation == '+':
                result = add(number_1, number_2)
            elif operation == '-':
                result = subtract(number_1, number_2)
            elif operation == '*':
                result = multiply(number_1, number_2)
            elif operation == '/':
                result = divide(number_1, number_2)
            print("Result:", result)
            break
        except Exception as e:
            print("Error:", e)
calculator()
