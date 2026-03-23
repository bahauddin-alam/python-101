# LECTURE 14. part:1 — Numbers, Booleans and Operators in Python
# Demonstrating integer numbers and common arithmetic operators


# Integer values (whole numbers)
black_tea_grams = 14
ginger_tea_grams = 3


# Addition operator (+) → adds two numbers
total_grams = black_tea_grams + ginger_tea_grams
print(f"total grams of base tea is {total_grams}")


# Subtraction operator (-) → subtracts one number from another
remaining_grams = black_tea_grams - ginger_tea_grams
print(f"total grams of remaining tea is {remaining_grams}")


milk_litres = 7
servings = 4


# Division operator (/) → returns a floating point number (decimal result)
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")


total_tea_bags = 7
pots = 4 


# Floor division operator (//)
# Divides numbers and removes the decimal part (returns an integer result)
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot: {bags_per_pot}")


total_cardamon_pods = 10
pods_per_cup = 3


# Modulus operator (%) → returns the remainder of a division
leftover_pods = total_cardamon_pods % pods_per_cup
print(f"Leftover cardamon pods {leftover_pods}")


# Exponent operator (**) → raises a number to a power
# Example: 2**3 = 2 * 2 * 2
base_flavour_strength = 2
scale_factor = 3

powerful_flavour = base_flavour_strength ** scale_factor
print(f"Scaled flavour strength {powerful_flavour}")


# Large numbers can be written using underscores (_) for readability
# Python ignores the underscores
total_leaves_harvested = 1_000_000_000
print(f"Tea leaves: {total_leaves_harvested}")