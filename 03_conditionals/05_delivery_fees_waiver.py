#LECTURE 26. Delivery Fees Waiver System

"""
26. Delivery Fees Waiver System
You run an online tea store.
If the order amount is more than ₹300, delivery is free;
otherwise, it costs ₹30.
Task:
• Input: order_amount
• Use ternary operator to decide delivery fee
Only Python course that you need
"""

# Delivery Fees Waiver System
# The program decides whether delivery is free based on the order amount


# Take order amount input from the user
order_amount = int(input("Enter the order amount: "))


# Ternary (conditional) operator
# If order_amount > 300 → delivery fee = 0 (free delivery)
# Else → delivery fee = 30
delivery_fees = 0 if order_amount > 300 else 30


# Display the delivery fee
print(f"Delivery fees is : {delivery_fees}")