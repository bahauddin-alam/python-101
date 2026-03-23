# LECTURE 14 — Part 3: Numbers, Booleans and Operators in Depth (Floating Point)

# sys module provides information about Python runtime and system details
import sys

# fractions module allows precise rational number calculations (like 1/3 exactly)
from fractions import Fraction

# decimal module provides high-precision decimal arithmetic
# useful for financial or scientific calculations where float precision matters
from decimal import Decimal


# Floating point numbers (decimal numbers)
ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal temp {ideal_temp}")
print(f"Current temp {current_temp}")


# Subtracting floating point numbers
# Sometimes floating point arithmetic may show small precision errors
print(f"Difference temp {ideal_temp - current_temp}")


# sys.float_info shows details about how Python stores float numbers
# (precision, max value, min value, epsilon etc.)
print(sys.float_info)