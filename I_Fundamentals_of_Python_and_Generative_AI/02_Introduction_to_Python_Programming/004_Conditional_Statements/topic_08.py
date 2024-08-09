opened_file = open("daily_sales.txt")
selected_orders = []

for order in opened_file:
    order_list = order.split(",")
    order_number = order_list[0]
    products = order_list[1]
    purchase_total = float(order_list[2])

    if not purchase_total > 100 and not purchase_total < 50:
        selected_orders.append(order_number)

opened_file.close()

print(selected_orders)
