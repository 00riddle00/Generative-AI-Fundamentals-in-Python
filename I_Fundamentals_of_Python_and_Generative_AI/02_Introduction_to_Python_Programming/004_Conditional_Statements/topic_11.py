opened_file = open("daily_sales.txt")
discounted_orders = []

for order in opened_file:
    order_list = order.split(",")
    order_number = order_list[0]
    products = order_list[1]
    products_str = products[1:-1]
    products_list = products_str.split(";")
    if "Headphones" in products_list:
        discounted_orders.append(order_number)

opened_file.close()

print(discounted_orders)
