essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices # This is called union of sets by |
print(f"All spices {all_spices}")

common_spices = essential_spices & optional_spices # This is called intersection of sets by &
print(f"Common spices {common_spices}")

only_in_essential = essential_spices - optional_spices # This is called unqiue items in a set -
print(f"Only in essential spices {only_in_essential}")

print(f"Is cloves in optional spices: {'cloves' in optional_spices}")

#There is also a set called FROZEN SET refer ai for this or wait for it in future...
"""It is an immutable unordered collection of unique elements."""