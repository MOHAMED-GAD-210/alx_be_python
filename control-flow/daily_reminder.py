# File: daily_reminder.py

# Ask the user for the task
task = input("Enter your task: ")

# Ask for the priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if it is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use Match Case to handle priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an undefined priority"

# Modify the message if the task is time-bound
if time_bound == "yes" and priority in ["high", "medium"]_
