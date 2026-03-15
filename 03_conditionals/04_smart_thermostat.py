#LECTURE 25. Building Smart Thermostat System

"""
You're building a smart thermostat alert system:
• If the device_status is "active"
• And temperature > 35 → Warn: "High temperature alert!"
• Else: "Temperature normal"
• If device is off → "Device is offline"
"""

# Smart thermostat alert system
# The program checks if the device is active and monitors the temperature


# Device status and temperature values
device_status = "active"
temperature = 38


# First check if the device is active
if device_status == "active":

    # Nested condition: check temperature level
    if temperature > 35:
        # Warning if temperature is too high
        print("High temperature alert!")
    else:
        # If temperature is within normal range
        print("Temperature is normal")

else:
    # If the device is not active
    print("Device is offline")