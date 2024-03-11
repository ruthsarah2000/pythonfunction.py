'''
8. The Journey Planner
Objective:
The aim of this assignment is to create a program that plans a journey, calculating travel times and stops.

Task 1: Code a function that calculates travel time based on distance and speed.
Task 2: Create a feature that suggests stops based on the length of the journey.
Task 3: Implement user input for starting point, destination, and preferred travel speed.
'''

def travel_time(distance, speed):
    time = distance / speed
    return time

def suggest_stops(distance):
    stops = []
    if distance > 200:
        stops.append("Rest Area")
    if distance > 400:
        stops.append("Scenic Viewpoint")
    if distance > 600:
        stops.append("Historic Landmark")
    return stops

def main():
    start = input("Enter your starting point ('Chicago', 'Michigan', 'Ohio'): ").capitalize()
    destination = input("Enter your destination ('Michigan', 'Ohio', 'Kentucky'): ").capitalize()
    speed = int(input("Enter your preferred travel speed (miles per hour): "))

    if start not in ['Chicago', 'Michigan', 'Ohio'] or destination not in ['Michigan', 'Ohio', 'Kentucky']:
        print("Invalid starting point or destination.")
        return

    
    distances = {
        ('Chicago', 'Michigan'): 200,
        ('Michigan', 'Ohio'): 300,
        ('Ohio', 'Kentucky'): 400
    }
    distance = distances.get((start, destination))
    if distance is None:
        print("Invalid route.")
        return

   
    time = travel_time(distance, speed)
    print(f"Estimated travel time from {start} to {destination}: {time:.2f} hours")

   
    stops = suggest_stops(distance)
    if stops:
        print("Suggested stops along the way:")
        for stop in stops:
            print(stop)

if __name__ == "__main__":
    main()          
