# LECTURE -- 13. part:2 Objects - Mutable and Immutable in Python

"""
# Mutable vs Immutable (Python)

# Mutable:
# Same object, same id, same memory location
# Contents can be modified in-place (efficient for frequently changing data)
# Examples: list, set, dict

# Immutable:
# Changing the value creates a new object (safer and predictable)
# Original object cannot be modified
# Examples: int, str, tuple, bool

# Key idea:
# Mutable → contents change/modified --->>>The "Whiteboard"
# Immutable → new object created --->>>The "Printed Paper"
"""

spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {spice_mix}")
spice_mix.add("Ginger")
spice_mix.add("Cardamon")
print(f"Initial spice mix id: {spice_mix}")
print(f"After spice mix id: {id(spice_mix)}")