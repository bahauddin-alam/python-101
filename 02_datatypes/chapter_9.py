# LECTURE 19 — Sets and Frozensets in Python


#Set: unordered collection of unique elements (no duplicates allowed)
essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}


# Union (|) → combines all unique elements from both sets
all_spices = essential_spices | optional_spices
print(f"All spices {all_spices}")


# Intersection (&) → elements common to both sets
common_spices = essential_spices & optional_spices
print(f"Common spices {common_spices}")


# Difference (-) → elements present in the first set but not in the second
only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices {only_in_essential}")


# Membership testing using 'in'
# Checks if an element exists inside the set
print(f"Is cloves in optional spices: {'cloves' in optional_spices}")


# Frozenset:
# Immutable version of a set (cannot add or remove elements)
# Used when you need a fixed set of values
# Example:
# frozen_spices = frozenset({"cardamon", "ginger", "cinnamon"})