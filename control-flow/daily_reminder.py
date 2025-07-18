# daily_reminder.py

# Get user input
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Loop once for demonstration purpose
for _ in range(1):
    # Match Case based on priority (Python 3.10+)
    match priority:
        case "high":
            message = f"'{task}' is a high priority task."
        case "medium":
            message = f"'{task}' is a medium priority task."
        case "low":
            message = f"'{task}' is a low priority task."
        case _:
            message = f"'{task}' has an unrecognized priority level."

    # Time sensitivity check
    if time_bound == "yes":
        message += " That requires immediate attention today!"
    elif time_bound == "no":
        message += " Consider completing it when you have free time."
    else:
        message += " (Time sensitivity not understood.)"

    print("\nReminder:", message)
