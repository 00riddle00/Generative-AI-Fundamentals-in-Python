opened_file = open("daily_sales.txt")
selected_orders = []
total_rebates = 5

for order in opened_file:
    order_list = order.split(",")
    order_number = order_list[0]
    products = order_list[1]
    purchase_total = float(order_list[2])
    products_str = products[1:-1]
    products_list = products_str.split(";")
    if "Printer" in products_list:
        continue
    else:
        total_rebates -= 1
        selected_orders.append(order_number)
        print("Rebate delivered for order #", order_number)
    if total_rebates == 0:
        break

opened_file.close()
