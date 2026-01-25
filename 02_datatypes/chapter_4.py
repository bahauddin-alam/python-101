#LECTURE -- 14. Numbers, Booleans and Operators in Depth in Python

is_boiling = True
stri_count = 5
Total_actions = stri_count + is_boiling # it is called upcasting
print(f"Total actions: {Total_actions}")

milk_present = 0  # no milk
print(f"Is there milk {bool(milk_present)}")

light_on = 1 # switch on 
print(f"Is light on {bool(light_on)}")

is_cold = None # Means Fasle or 0
print(f"Is cold {bool(is_cold)}") 


is_okay = "Alam" # EXCEPT 0, FLASE OR NONE everyhting is a TRUE in python
print(f"Is okay {bool(is_okay)}")


#Logical operations OR, AND, NOT
water_hot = True
tea_added = False
#AND
can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")

gmail = True
username = False
#OR
can_login = gmail or username
print(f"Can login? {can_login}")

#NOT
user_authenticated = True

# Check if user is NOT authenticated
can_access_content = not user_authenticated
print(f"Can access content if user is not authenticated? {can_access_content}")

#Another examplf of NOT
is_premium_member = True

if not is_premium_member:
    print("Access to this feature is granted.")
else:
    print("Premium members cannot access this feature.")
