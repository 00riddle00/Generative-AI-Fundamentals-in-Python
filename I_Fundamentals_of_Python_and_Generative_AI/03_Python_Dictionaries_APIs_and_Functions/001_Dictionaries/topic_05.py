laptop_product = {
    "name": "Laptop",
    "price": 899.00,
    "currency": "USD",
    "quantity": 2,
    "user_rating": 3.34,
    "category": "Hardware",
}

currency_rates = {
    "EUR": 0.85,
    "GBP": 0.72,
    "JPY": 109.35,
    "CAD": 1.21,
}

is_in_dict_1 = "price" in laptop_product
is_in_dict_2 = "CAD" in currency_rates

if "price" in laptop_product:
    laptop_price = laptop_product["price"]
    print(laptop_price)

if "CAD" in currency_rates:
    cad_rate = currency_rates["CAD"]
    print(cad_rate)

if "price" in laptop_product and "CAD" in currency_rates:
    converted_price = laptop_price * cad_rate
    print(converted_price)
