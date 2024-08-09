opened_file = open("daily_sales.txt")

orders_50_and_under = []

for order in opened_file:
    order_list = order.split(",")
    order_number = order_list[0]
    purchase_total = float(order_list[2])
    if purchase_total <= 50:
        orders_50_and_under.append(order_number)

opened_file.close()

print(orders_50_and_under)
