# LECTURE -- 13. Objects - Mutable and Immutable in Python

spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {spice_mix}")
spice_mix.add("Ginger")
spice_mix.add("Cardamon")
print(f"Initial spice mix id: {spice_mix}")
print(f"After spice mix id: {id(spice_mix)}")


#"Cannot add/update the original. Instead, we copy old + new info to a new place.FOR IMMUTABLES, has fixed space in memory"
#here id changes for immutable cuz it has fix space in memory and 
# if gets added new things it goes to new place in memory and place changes and deleted 
#Mutable can change items in it but has fixed place in memory and has fixed ID and but has extra space in memory