#LECTURE -- 14. Numbers, Booleans and Operators in Depth in Python

#Integer

black_tea_grams = 14
ginger_tea_grams = 3

#Add +

total_grams = black_tea_grams + ginger_tea_grams
print(f"total grams of base tea is {total_grams}")

#Subtract -

remaining_grams = black_tea_grams - ginger_tea_grams
print(f"total grams of remaining tea is {remaining_grams}")


milk_litres = 7
servings = 4

#Divide /

milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")


total_tea_bags = 7
pots = 4 

#Divide without getting any floating numbers or any decimal no. is //

bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot: {bags_per_pot}")


total_cardamon_pods = 10
pods_per_cup = 3

#Remiander finding method is %

leftover_pods = total_cardamon_pods % pods_per_cup
print(f"Leftover cardamon pods {leftover_pods}")

#Exponent **

base_flavour_strength = 2
scale_factor = 3

powerful_flavour = base_flavour_strength ** scale_factor
print(f"Scaled flavour strength {powerful_flavour}")
#here is 2*2*2


#Big number written using underscores
total_leaves_harvested = 1_000_000_000
print(f"Tea leaves: {total_leaves_harvested}")