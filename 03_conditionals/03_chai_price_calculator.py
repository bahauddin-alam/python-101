#LECTURE 24. Building a Chai Price Calculator

"""
Tea stall pricing system
The program calculates the price of chai based on the selected cup siz

Take cup size input from the user
.lower() ensures input comparison works even if user types SMALL/Small/etc.
"""
cup = input("Choose your cup size (small/medium/large): ").lower()


# Conditional pricing using if-elif-else
# Only one matching condition will run
if cup == "small":
    print("Your price is 10 rs")

elif cup == "medium":
    print("Your price is 15 rs")

elif cup == "large":
    print("Your price is 20 rs")

else:
    # Runs if the input does not match any valid size
    print("Unknown cup size")