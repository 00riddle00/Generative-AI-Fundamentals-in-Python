currency_rates = {"EUR": 0.85, "GBP": 0.72, "JPY": 109.35, "CAD": 1.21}
orders = {}

opened_file = open("global_daily_sales.txt")
for order in opened_file:
    order_list = order.split(",")
    order_number = int(order_list[0])
    sales_total = float(order_list[1])
    country_currency = order_list[2].rstrip()
    if order_number not in orders:
        orders[order_number] = {
            "sales_total": sales_total,
            "currency": country_currency,
        }
opened_file.close()

for order in orders:
    currency = orders[order]["currency"]
    total = orders[order]["sales_total"]
    if currency != "USD":
        conversion_rate = currency_rates[currency]
        orders[order]["sales_total"] = total / conversion_rate
        orders[order]["currency"] = "USD"

print(orders)
