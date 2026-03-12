# Cafe snack suggestion system
# The program checks if the requested snack is available in the cafe


# Take snack input from the user
# .lower() converts input to lowercase to make comparison easier
snack = input("Enter your preferred snack: ").lower()


# Check if the snack is either "cookies" or "samosa"
# 'or' means at least one condition must be True
if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
    # If the snack is not available in the menu
    print("Sorry, we only serve cookies or samosa with tea")