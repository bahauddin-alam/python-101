#LECTURE 27. Build a train seat information system

"""
You're building a ticket info system for a railway app. Based on seat type, show its features.

Task:
- Input: "sleeper", "AC", "general", "luxury"
- Match using match-case
- Unknown → show: "Invalid seat type"

Only Python course that you need
"""

# Railway ticket seat information system
# The program displays seat features based on the seat type selected by the user


# Take seat type input from the user
# .lower() ensures the input matches the cases even if user types AC/Ac/etc.
seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()


# match-case is Python's pattern matching (similar to switch-case in other languages)
match seat_type:

    # Each case checks a possible value of seat_type
    case "sleeper":
        print("Sleeper - No AC, beds available")

    case "ac":
        print("AC - Air conditioned, comfy ride")

    case "general":
        print("General cheapest option, no reservation")

    case "luxury":
        print("Luxury - Premium seats with meals")

    # case _ acts as a default case for unmatched inputs
    case _:
        print("Invalid seat type")