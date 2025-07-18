# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Loop runs once — demonstrating loop usage in structure
for _ in range(1):
    # Match Case statement for priority
    match priority:
        case "high":
            message = f"'{task}' is a high priority task."
        case "medium":
            message = f"'{task}' is a medium priority task."
        case "low":
            message = f"'{task}' is a low priority task."
        case _:
            message = f"'{task}' has an unknown priority level."

    # Add time sensitivity messaging
    if time_bound == "yes":
        message += " That requires immediate attention today!"
    elif time_bound == "no":
        message += " Consider completing it when you have free time."
    else:
        message += " (Time sensitivity input not recognized.)"

    print("\nReminder:", message)
