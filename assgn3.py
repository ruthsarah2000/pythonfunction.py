'''
3. The Temperature Converter
Objective:
The aim of this assignment is to write a program that converts temperatures between Fahrenheit and Celsius.

Task 1: Code a function that converts Celsius to Fahrenheit.
Task 2: Code a function that converts Fahrenheit to Celsius.
Task 3: Implement a user interface that asks the user which conversion they want to perform and calls the appropriate function.
'''

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Choose conversion:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter choice (1 or 2): ")

if choice == '1':
    temperature = float(input("Enter temperature in Celsius: "))
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is equivalent to {converted_temperature}°F")
elif choice == '2':
    temperature = float(input("Enter temperature in Fahrenheit: "))
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is equivalent to {converted_temperature}°C")
else:
    print("Invalid choice. Please enter 1 or 2.")
