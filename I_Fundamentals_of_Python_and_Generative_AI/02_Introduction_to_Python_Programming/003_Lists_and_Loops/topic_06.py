mouse_product = ["Mouse", 13.99, "USD", 14, 2.45]

mouse_product.append("Peripherals")
print(mouse_product)

category = mouse_product[-1]
mouse_product.remove(category)
print(mouse_product)
