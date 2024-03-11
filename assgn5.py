'''
5. The Grade Analyzer
Objective:
The aim of this assignment is to analyze a set of grades and provide statistics.

Task 1: Code a function to calculate the average grade.
Task 2: Implement a function to find the highest and lowest grade.
Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
'''



def average_grade(grade):
    avg_grade = sum(grade)/len(grade)
    return avg_grade


grade = [99, 54, 45, 89, 72, 66, 74]
average = average_grade(grade)
print(f"Average Garde: {average:.2f}")

lowest_grade = min(grade)
print("Lowest Grade:", lowest_grade)

highest_grade = max(grade)
print("Highest Grade:", highest_grade)

def letter_grade(score):
    if score > 90:
        return "Grade A"
    elif score > 80:
        return "Grade B"
    elif score > 70:
        return "Grade C"
    elif score > 60:
        return "Grade D"
    else:
        return "Grade F"
    
for grade in grade:
    print(f"Grade, {letter_grade(grade)}")
