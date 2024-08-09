import random

products = [
    "Laptop",
    "Printer",
    "Keyboard",
    "Mouse",
    "HDMI Cable",
    "Headphones",
    "Docking Station",
]

random_product = random.choice(products)
print(random_product)

random_index = random.randint(1, 6)
print(products[random_index])
