"""Should You Go for a Walk?
You’re deciding whether to go for a walk based on two real-life conditions:
    is_sunny = True
    have_umbrella = False

Print the result of the following:
    Is it not sunny today?
    Do you not have an umbrella?
    Should you go for a walk if it’s sunny and you don’t need an umbrella?
    Should you go for a walk if it’s sunny or if you have an umbrella?
"""


is_sunny = True
have_umbrella = False

print(f"Is it not sunny today? {not is_sunny}")
print(f"Do you not have an umbrella? {not have_umbrella}")
print(f"Should you go for a walk if it’s sunny and you don’t need an umbrella? {is_sunny and not have_umbrella}")
print(f"Should you go for a walk if it’s sunny or if you have an umbrella? {is_sunny or have_umbrella}")