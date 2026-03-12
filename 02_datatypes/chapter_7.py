# LECTURE 16 — Tuples and Membership Testing


# Tuple: an ordered and immutable collection of items
# Order is fixed and elements cannot be changed after creation
masala_spices = ("cardamon", "cloves", "cinnamon")


# Tuple unpacking: assigning tuple elements to separate variables
(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")


# Multiple variable assignment
ginger_ratio, cardamon_ratio = 2, 1
print(f"Ratio is G :{ginger_ratio} and C: {cardamon_ratio}")


# Python allows easy value swapping using tuple unpacking
ginger_ratio, cardamon_ratio = cardamon_ratio, ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cardamon_ratio}")


# Membership testing using 'in'
# Checks whether a value exists inside a sequence (tuple, list, string, etc.)
print(f"Is ginger in masala spices? {'ginger' in masala_spices}")
print(f"Is cloves in masala spices? {'cloves' in masala_spices}")