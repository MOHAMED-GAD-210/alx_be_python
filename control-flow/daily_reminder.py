# File: daily_reminder.py

# Ask the user for the task
task = input("Enter your task: ")

# Ask for the priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if it is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use Match Case to handle priority and print directly
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task.")
    case "low":
        if time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Reminder: '{task}' is a low priority task.")
    case _:
        print(f"Reminder: '{task}' has an undefined priority")
