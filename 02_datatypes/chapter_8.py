#LECTURE -- 17. Basics of List in Python

ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar") # Adding mrthod
print(f"Ingredients are {ingredients}")

ingredients.remove("water") #removing things from list method
print(f"Updated ingredients are {ingredients}")

spice_options = ["ginger", "cardamon"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options) #combing lists method
print(f"Chai extend: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")
print(f"Chai insert: {chai_ingredients}")

last_added = chai_ingredients.pop() #Variable declearing and removing things from list as variable
print(f" pop varible out {last_added}")
print(f"Chai after pop: {chai_ingredients}")

chai_ingredients.reverse() #Reversing the order of the list
print(f"Chai reverse: {chai_ingredients}")

chai_ingredients.sort() # By numerical or aplhabetical order
print(f"Chai sort: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5] #Taking out max
"""Returns the item with the highest or lowest value/rank. The list remains unchanged.
Numbers vs. Numbers: Works (Magnitude) 
Strings vs. Strings: Works (Alphabetical)."""

print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Min sugar level: {min(sugar_levels)}")

