#!/usr/bin/env python3
"""
Daily Reminder Script
A simple Python script that uses conditional statements, Match Case, and loops
to provide customized task reminders based on priority and time sensitivity.
"""

def get_user_input():
    """Get task details from user with input validation."""
    
    # Get task description
    while True:
        task = input("Enter your task: ").strip()
        if task:
            break
        print("Please enter a valid task description.")
    
    # Get priority with validation loop
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ['high', 'medium', 'low']:
            break
        print("Please enter 'high', 'medium', or 'low'.")
    
    # Get time-bound status with validation loop
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'.")
    
    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
    """Generate a customized reminder using Match Case and conditional statements."""
    
    # Use Match Case to handle different priority levels
    match priority:
        case 'high':
            base_message = f"'{task}' is a high priority task"
            if time_bound == 'yes':
                reminder = f"Reminder: {base_message} that requires immediate attention today!"
            else:
                reminder = f"Reminder: {base_message}. Make sure to complete it soon!"
        
        case 'medium':
            base_message = f"'{task}' is a medium priority task"
            if time_bound == 'yes':
                reminder = f"Reminder: {base_message} that requires immediate attention today!"
            else:
                reminder = f"Note: {base_message}. Plan to complete it this week."
        
        case 'low':
            base_message = f"'{task}' is a low priority task"
            if time_bound == 'yes':
                reminder = f"Reminder: {base_message} that requires immediate attention today!"
            else:
                reminder = f"Note: {base_message}. Consider completing it when you have free time."
        
        case _:  # Default case (shouldn't reach here due to validation)
            reminder = f"Note: '{task}' needs attention."
    
    return reminder

def main():
    """Main function that orchestrates the daily reminder process."""
    
    print("=== Daily Task Reminder ===")
    print("Let's set up your priority task for today!\n")
    
    # Loop to allow multiple reminders or exit
    while True:
        try:
            # Get user input
            task, priority, time_bound = get_user_input()
            
            # Generate and display reminder
            reminder = generate_reminder(task, priority, time_bound)
            print(f"\n{reminder}\n")
            
            # Ask if user wants to set another reminder
            while True:
                continue_choice = input("Would you like to set another reminder? (yes/no): ").strip().lower()
                if continue_choice in ['yes', 'no']:
                    break
                print("Please enter 'yes' or 'no'.")
            
            if continue_choice == 'no':
                print("Have a productive day! 🚀")
                break
            else:
                print()  # Add blank line for readability
                
        except KeyboardInterrupt:
            print("\n\nGoodbye! Have a great day! 👋")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()