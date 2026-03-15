# LECTURE 21 — Touch on Advanced Data Types (Libraries & Collections)

"""
'arrow' is a third-party library used for easier date and time handling
It improves on Python's built-in datetime module
"""

import arrow

# Get the current UTC time
brewing_time = arrow.utcnow()

# Convert time to another timezone (example: Europe/Rome)
brewing_time.to("Europe/Rome")


# 'collections' module provides specialized container data types
from collections import namedtuple


# namedtuple → creates lightweight objects similar to tuples
# but with named fields for better readability
chaiProfile = namedtuple("chaiProfile", ["flavour", "aroma"])

# Example usage (optional idea)
# chai = chaiProfile("spicy", "strong")
# print(chai.flavour)