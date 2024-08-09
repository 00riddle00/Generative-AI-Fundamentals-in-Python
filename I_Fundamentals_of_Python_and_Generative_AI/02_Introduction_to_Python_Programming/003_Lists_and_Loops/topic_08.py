new_orders = ["Laptop,Keyboard,Mouse", "Printer,HDMI Cable", "Mouse"]

for order in new_orders:
    ordered_products = order.split(",")
    print(len(ordered_products))
    print(ordered_products)
