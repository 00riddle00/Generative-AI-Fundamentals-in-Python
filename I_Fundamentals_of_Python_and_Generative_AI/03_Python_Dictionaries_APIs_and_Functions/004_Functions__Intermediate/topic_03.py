import requests


def convert_amount(amount, target_currency, original_currency="USD"):
    url = "https://api.exchangerate-api.com/v4/latest/" + original_currency
    response = requests.get(url)
    data = response.json()

    # Extract the exchange rate for the desired currency
    exchange_rate = data["rates"][target_currency]
    converted_amount = amount * exchange_rate
    return converted_amount


converted_amount_1 = convert_amount(100, "CAD")
converted_amount_2 = convert_amount(100, "CAD", "EUR")

print(converted_amount_1)
print(converted_amount_2)
