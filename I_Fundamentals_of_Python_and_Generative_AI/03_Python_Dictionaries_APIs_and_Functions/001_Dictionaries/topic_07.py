opened_file = open("global_daily_sales.txt")

country_counts = {}
for order in opened_file:
    order_list = order.split(",")
    country_currency = order_list[2].rstrip()

    if country_currency in country_counts:
        country_counts[country_currency] += 1
    else:
        country_counts[country_currency] = 1

opened_file.close()

print(country_counts)
