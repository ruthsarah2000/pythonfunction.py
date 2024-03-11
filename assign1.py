'''
1. The Welcoming Program
Objective:
The aim of this assignment is to create a simple program that greets users and responds based on their input.

Task 1: Code a program that asks for the user's name and prints a personalized greeting.
Task 2: Modify the program to ask the user how they are feeling today and respond with a comforting message if they're feeling down, or a cheerful one if they're happy.
Task 3: Add error handling to ensure that the user inputs a string for their name and not a number or special character.
'''
''' Task 1 '''
greeting = input("Hello! What is your name?:\nI hope you are having a great day!")

print(greeting)

''' Task 2'''
greeting = input("How are you feeling today?\nType a for happy or b for sad: ")
happy = "a"
sad = "b"

print (greeting)
if greeting == happy:
    print("Great! Things will only look brighter today!")
elif greeting == sad:
    print("Oh no! Don't worry, things can only get better from her.")
else:
    print("Invalid entry, you can only type a or b.")

'''Task 3'''
greeting = input("Hello! I hope you are having a good day!")
while True:
    user_input = input("What is your name?: ")
    if user_input.isalpha():
        break
    else:
        print("Invalid input! Please enter only alphabetic characters.")

print("Hi!", user_input)

