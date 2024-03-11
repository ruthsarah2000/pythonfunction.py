'''
10. The Fitness Tracker
Objective:
The aim of this assignment is to create a program that tracks fitness activities and calories burned.

Task 1: Develop a function to log different fitness activities and their duration.
Task 2: Write a function that estimates calories burned based on the activity and duration.
Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

Each of these assignments is designed to challenge the learner to apply the concepts discussed, such as user input, 
type conversion, string formatting, and function creation, while also ensuring they practice error handling and user-friendly output formatting.
'''

def log_fitness_activity(activity, duration, log):
    
    log[activity] = duration

def estimate_calories_burned(activity, duration):
    
    calorie_values = {'jog': 10, 'walk': 5, 'yoga': 3, 'cycling': 8}
    calorie_per_minute = calorie_values.get(activity, 1)  # Default value: 1 calorie per minute
    duration_minutes = int(duration.split()[0])  # Extract duration in minutes
    return calorie_per_minute * duration_minutes

def generate_summary(log):
    
    summary = "Fitness Activity Summary:\n"
    total_calories = 0
    for activity, duration in log.items():
        calories_burned = estimate_calories_burned(activity, duration)
        total_calories += calories_burned
        summary += f"- {activity}: {duration}, Calories Burned: {calories_burned}\n"
    summary += f"Total Calories Burned: {total_calories}"
    return summary

log = {}
log_fitness_activity('jog', '30 mins', log)
log_fitness_activity('cycling', '20 mins', log)
log_fitness_activity('walk', '45 mins', log)
log_fitness_activity('yoga', '25 mins', log)
print(generate_summary(log))
