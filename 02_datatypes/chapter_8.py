# LECTURE 17 — Basics of Lists
# LECTURE 18 — Operator Overloading and bytearray in Python


# List: ordered and mutable collection (items can be added, removed, modified)
ingredients = ["water", "milk", "black tea"]

# append() → adds an item at the end of the list
ingredients.append("sugar")
print(f"Ingredients are {ingredients}")


# remove() → removes a specific value from the list
ingredients.remove("water")
print(f"Updated ingredients are {ingredients}")


spice_options = ["ginger", "cardamon"]
chai_ingredients = ["water", "milk"]

# extend() → adds elements from another list to the current list
chai_ingredients.extend(spice_options)
print(f"Chai extend: {chai_ingredients}")


# insert(index, value) → inserts an item at a specific position
chai_ingredients.insert(2, "black tea")
print(f"Chai insert: {chai_ingredients}")


# pop() → removes and returns the last element (or given index)
last_added = chai_ingredients.pop()
print(f"pop variable out {last_added}")
print(f"Chai after pop: {chai_ingredients}")


# reverse() → reverses the order of the list
chai_ingredients.reverse()
print(f"Chai reverse: {chai_ingredients}")


# sort() → sorts the list alphabetically or numerically
chai_ingredients.sort()
print(f"Chai sort: {chai_ingredients}")


# max() and min() → return highest or lowest value in a list
# Works with numbers (magnitude) and strings (alphabetical order)
sugar_levels = [1, 2, 3, 4, 5]

print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Min sugar level: {min(sugar_levels)}")


# Operator overloading with lists
# '+' combines lists and creates a new list (similar to extend but returns new list)
base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Mixed liquid: {full_liquid_mix}")


# '*' repeats list elements multiple times
strong_brew = ["black tea", "water"] * 3
print(f"Print strong brew: {strong_brew}")


# bytearray → mutable sequence of bytes (used for low-level binary data)
raw_spice_data = bytearray(b"CINNAMON")

# replace() modifies the byte content
raw_spice_data = raw_spice_data.replace(b"CINN", b"CARD")
print(f"Bytes: {raw_spice_data}")


# split() → converts a string into a list by splitting at a separator
# Default separator is whitespace
veggie_string = "tomato cucumber spinach"

veggie_list = veggie_string.split()
print(f"Converted List: {veggie_list}")