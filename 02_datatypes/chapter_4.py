# LECTURE 14. part:2 — Numbers, Booleans and Logical Operators in Python


# Boolean values: True and False
is_boiling = True

# In Python, bool behaves like an integer
# True = 1 and False = 0
stri_count = 5

# When bool is used in arithmetic, it is automatically converted to int
# True → 1, False → 0 (implicit type conversion / upcasting)
Total_actions = stri_count + is_boiling
print(f"Total actions: {Total_actions}")


# Converting values to Boolean using bool()

milk_present = 0  # 0 is treated as False
print(f"Is there milk {bool(milk_present)}")

light_on = 1  # any non-zero number is True
print(f"Is light on {bool(light_on)}")


# None represents absence of value and is treated as False in boolean context
is_cold = None
print(f"Is cold {bool(is_cold)}") 


# Non-empty strings are True
# In Python everything except 0, False, None, or empty values is True
is_okay = "Alam"
print(f"Is okay {bool(is_okay)}")


# Logical Operators: AND, OR, NOT


# AND → True only if both conditions are True
water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can serve chai? {can_serve}")


# OR → True if at least one condition is True
gmail = True
username = False

can_login = gmail or username
print(f"Can login? {can_login}")


# NOT → reverses the boolean value (True becomes False and vice versa)
user_authenticated = True

# Check if user is NOT authenticated
can_access_content = not user_authenticated
print(f"Can access content if user is not authenticated? {can_access_content}")


# Another example of NOT
is_premium_member = True

# Feature available only for non-premium users
if not is_premium_member:
    print("Access to this feature is granted.")
else:
    print("Premium members cannot access this feature.")