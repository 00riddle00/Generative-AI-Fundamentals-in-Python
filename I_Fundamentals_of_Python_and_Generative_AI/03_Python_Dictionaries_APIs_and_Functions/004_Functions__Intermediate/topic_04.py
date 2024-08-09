import requests

response = requests.get("https://api.exchangerate-api.com/v4/latest/usd")
exchange_rates = response.json().get("rates")
jpy_exchange_rate = exchange_rates["JPY"]


def convert_currency(exchange_rate, amount):
    """This function multiples the exchange rate by the amount to convert"""
    converted_amount = exchange_rate * amount
    return converted_amount


jpy_value = convert_currency(exchange_rate=jpy_exchange_rate, amount=235.23)

print(jpy_value)

rounded_jpy_value_1 = round(jpy_value, 2)
rounded_jpy_value_2 = round(jpy_value, ndigits=2)

print(rounded_jpy_value_1)
print(rounded_jpy_value_2)
