opened_file = open("daily_sales.txt")
selected_orders = []

for order in opened_file:
    order_list = order.split(",")
    order_number = order_list[0]
    products = order_list[1]
    purchase_total = float(order_list[2])
    products_str = products[1:-1]
    products_list = products_str.split(";")

    for product in products_list:
        product_name = product.split(":")[0]
        if (
            product_name == "Printer"
            and purchase_total >= 100
            and purchase_total <= 500
        ):
            selected_orders.append(order_number)

opened_file.close()

print(selected_orders)
