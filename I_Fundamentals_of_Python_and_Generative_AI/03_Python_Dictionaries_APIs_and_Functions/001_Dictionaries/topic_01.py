laptop_price = 899.00
converted_amount = 0
conversion_rates = [["EUR", 0.85], ["GBP", 0.72], ["JPY", 109.35], ["CAD", 1.21]]

target_currency = "JPY"

for currency in conversion_rates:
    if currency[0] == target_currency:
        converted_amount = laptop_price * currency[1]
        break

print(converted_amount)
