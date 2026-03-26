"""
You're creating a tea menu board.
Each item must be numbered.
Task:
Use enumerate() to print menu items with numbers"
"""
print("TEA MENU")
print("-" * 20)

menu = ["Green", "Lemon", "Spiced", "Mint"]

for idx, item in enumerate(menu, start=1):
    print(f"{idx}: {item} chai")