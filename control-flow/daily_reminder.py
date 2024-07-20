def daily_reminder():
    # Prompt for a single task
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Process the task based on priority and time sensitivity
    reminder = ""

    # Use Match Case statement to react differently based on the task’s priority
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task."
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task."
        case "low":
            reminder = f"Note: '{task}' is a low priority task."
        case _:
            reminder = "Invalid priority. Please enter 'high', 'medium', or 'low'."

    # Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += " Consider completing it when you have free time."
    else:
        reminder = "Invalid time-bound input. Please enter 'yes' or 'no'."

    # Provide a customized reminder
    print(f"Reminder: '{reminder}' .")

# Run the main function
daily_reminder()
