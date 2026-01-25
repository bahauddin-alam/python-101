# LECTURE -- 16. Tuples and Membership Testing

masala_spices = ("cardamon", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamon_ratio = 2, 1

print(f"Ratio is G :{ginger_ratio} and C: {cardamon_ratio}")
ginger_ratio, cardamon_ratio = cardamon_ratio, ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cardamon_ratio}") # value is swapped in form of ratio

# membership testing it is checked by "in" checks the box, the, the purse, the container about belonging of specific material
print(f"Is ginger in masala spices? {'ginger' in masala_spices}")
print(f"Is cloves in masala spices? {'cloves' in masala_spices}")
