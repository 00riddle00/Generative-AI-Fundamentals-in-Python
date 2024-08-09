inventory_list = ["Laptop", "Printer", "Keyboard", "Mouse"]

print(len(inventory_list) == 4)

if len(inventory_list) < 5:
    print("We need more inventory!")

for item in inventory_list:
    print(item)
