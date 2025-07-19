# Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.
task = input("Enter your task: ")
priority = input("priority (high/medium/low): ").lower()
time_bond = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        if time_bond=="yes":
            print("Reminder: ", task,"is a high priority task that requires immediate attention today!")
        else:
            print("Reminder: ", task,"is a high priority task that requires attention today!")
    case "meduim":
        if time_bond=="yes":
            print("Alert: ", task,"is a meduim priority task that requires attention today!")
        else:
            print("Alert: ", task,"is a meduim priority task that requires attention today!")
    case "low":
        if time_bond=="yes":
            print("warrning: ", task,"is a low priority task that requires attention today!")
        else:
            print("Warrning: ", task,"is a low priority task that requires attention today!")