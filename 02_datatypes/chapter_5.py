#LECTURE -- 14. Numbers, Booleans and Operators in Depth in Python

import sys
from fractions import Fraction
from decimal import Decimal #here sir told about these libraries how they help such calculation and I get it little bit

ideal_temp = 95.5
current_temp = 95.49
print(f"Ideal temp {ideal_temp}")
print(f"Current temp {current_temp}")

print(f"Difference temp {ideal_temp - current_temp}")

print(sys.float_info)