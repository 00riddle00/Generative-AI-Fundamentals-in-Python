import requests


def convert_currency(exchange_rate, amount):
    """This function multiples the exchange rate by the amount to convert"""
    converted_amount = exchange_rate * amount
    rounded_converted_amount = round(converted_amount, 2)
    return converted_amount, rounded_converted_amount


response = requests.get("https://api.exchangerate-api.com/v4/latest/usd")
exchange_rates = response.json().get("rates")
jpy_exchange_rate = exchange_rates["JPY"]

jpy_values = convert_currency(jpy_exchange_rate, amount=235.23)
print(jpy_values)
