chai_order = dict(type = "Masala chai", size = "Large", sugar = 2)
print(f"Chai order:{chai_order}")

chai_recipe = {}
chai_recipe ["base"] = "black tea"
chai_recipe ["liquid"] = "milk"

print(f"Recipe base: {chai_recipe ['base']}")
print(f"Liquid: {chai_recipe['liquid']}")


print(f"All Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"All Recipe again: {chai_recipe}")

print(f"Is sugar in the order? {"sugar" in chai_order}")

chai_order = {"type": "Ginger chai", "Size": "Medium", "Sugar": "1"}
print(f"Order details(keys): {chai_order.keys()}")
print(f"Order details(values): {chai_order.values()}")
print(f"Order details(items): {chai_order.items()}")