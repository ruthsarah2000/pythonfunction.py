'''
7. The Quiz Game
Objective:
The aim of this assignment is to create a quiz game that asks questions and checks answers.

Task 1: Develop a list of questions and answers.
Task 2: Write a function that quizzes the user and takes their answers.
Task 3: Score the quiz and give the user feedback on their performance.
'''
import random

question_list = ['What color is the sky?', 'Where is Nemo?', 'Who is Shaggy?', 'Where is Arizona?']
answer_list = ['Blue', 'In the sea', 'Singer', 'South west']

def quiz():
    score = 0

    for question, answer in zip(question_list, answer_list):
        print(question)
        user_response = input("Type your guess of the listed responses: ('Blue', 'In the sea', 'Singer', 'South west'): ")
        if user_response == answer:
            print("Great job! You got it right.")
            score += 1
    else:
        print("Oh oh, that wasn't correct")
    return score

def score_quiz(score):
    total_questions = len(question_list)
    percentage = (score / total_questions) * 100
    
    print(f"\nYour score: {score}/{total_questions}")
    print(f"Percentage: {percentage}%")
    
    if percentage >= 75:
        print("WOW, Great job!")
    elif 50 <= percentage < 75:
        print("Not bad, but you can do better.")
    else:
        print("You definately need more practice.")

# Main function
def main():
    score = quiz()
    score_quiz(score)

if __name__ == "__main__":
    main()
