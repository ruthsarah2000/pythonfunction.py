'''
6. The Daily Planner
Objective:
The aim of this assignment is to create a simple daily planner that can add, remove, and display tasks.

Task 1: Write a function to add a task with a time slot.
Task 2: Code a function to remove a task.
Task 3: Implement a display function that shows all tasks in order of time.
'''

time_slots = ['0900', '1000', '1200', '1500', '1600']
tasks = ['Check emails', 'Conference call', 'Lunch', 'Doc Appt', 'Commute']

def manage_calendar():
    while True:
        print("\nDaily Planner")
        print("1. Add Task & Time")
        print("2. Remove Task & Time")
        print("3. All Tasks with Time")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_task = input("Enter the name of the new task: ")
            time = input("Enter the time (military format): ")
            tasks.append(new_task)
            time_slots.append(time)
            print(f"{new_task} has been added to the planner for {time}!")

        elif choice == "2":
            remove_task = input("Enter the name of the task to be removed: ")
            if remove_task in tasks:
                index = tasks.index(remove_task)
                del tasks[index]
                del time_slots[index]
                print(f"{remove_task} has been removed from the planner!")
            else:
                print("Task not found.")

        elif choice == "3":
            print("\nCurrent Planner:")
            for task, time in zip(tasks, time_slots):
                print(f"{time}: {task}")

        elif choice == "4":
            print("Exiting System")
            break

        else:
            print("Invalid selection, please try again.")

manage_calendar()
