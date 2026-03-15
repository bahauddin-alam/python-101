# LECTURE 20 — Dictionaries in Python


"""
Dictionary: collection of key-value pairs (mutable and unordered)
Keys must be unique
"""

chai_order = dict(type="Masala chai", size="Large", sugar=2)

print(f"Chai order: {chai_order}")


# Creating an empty dictionary and adding items
chai_recipe = {}

chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"


# Accessing values using keys
print(f"Recipe base: {chai_recipe['base']}")
print(f"Liquid: {chai_recipe['liquid']}")


# Printing entire dictionary
print(f"All Recipe: {chai_recipe}")


# Deleting a key-value pair using del
del chai_recipe["liquid"]

print(f"All Recipe again: {chai_recipe}")


# Membership testing checks keys (not values)
print(f"Is sugar in the order? {'sugar' in chai_order}")


# Dictionary with key-value pairs
chai_order = {"type": "Ginger chai", "Size": "Medium", "Sugar": "1"}


# keys() → returns all dictionary keys
print(f"Order details (keys): {chai_order.keys()}")

# values() → returns all dictionary values
print(f"Order details (values): {chai_order.values()}")

# items() → returns key-value pairs as tuples
print(f"Order details (items): {chai_order.items()}")


# popitem() → removes and returns the last inserted key-value pair
last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")


# update() → adds items from another dictionary
extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")


# Access value directly using key
chai_size = chai_order["Size"]
print(f"Chai size is: {chai_size}")


# get() → safely access a key (returns default if key not found)
customer_preference = chai_order.get("size", "No Preference")
print(f"Customer preference is: {customer_preference}")


# Note:
# Dictionary keys must be immutable (e.g., str, int, tuple)