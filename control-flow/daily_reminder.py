# daily_reminder.py

# Prompt the user to enter the task
task = input("Enter your task: ")

# Prompt the user to enter the priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide the customized reminder using match case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Note: '{task}' has an unknown priority. Please review it manually."

# Append time-bound message if needed
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder
print(reminder)
