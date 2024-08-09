opened_file = open("daily_sales.txt")
gold_orders = []
regular_orders = []

for order in opened_file:
    order_list = order.split(",")
    order_number = order_list[0]
    products = order_list[1]
    purchase_total = float(order_list[2])
    products_str = products[1:-1]
    products_list = products_str.split(";")

    if purchase_total >= 1000:
        gold_orders.append(order_number)
    else:
        regular_orders.append(order_number)

opened_file.close()

print(gold_orders)
