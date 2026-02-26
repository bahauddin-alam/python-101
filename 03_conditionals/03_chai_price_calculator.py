cup = input ("Choose your cup size (small/medium/large):").lower()

if cup == "small":
    print("Your price is 10 rs")
elif cup == "medium":
    print("Your price is 15 rs")
elif cup == "large":
    print("Your price is 20 rs")
else: 
    print("Unknown cup size")