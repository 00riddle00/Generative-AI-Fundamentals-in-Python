import requests


def convert_currency(exchange_rate, amount, round_result=True):
    """This function multiples the exchange rate by the amount to convert"""
    converted_amount = exchange_rate * amount
    if round_result:
        rounded_converted_amount = round(converted_amount, 2)
        return rounded_converted_amount
    else:
        return converted_amount


response = requests.get("https://api.exchangerate-api.com/v4/latest/usd")
exchange_rates = response.json().get("rates")
jpy_exchange_rate = exchange_rates["JPY"]

jpy_value = convert_currency(jpy_exchange_rate, amount=235.23)
print(jpy_value)

jpy_value_rounded = convert_currency(jpy_exchange_rate, amount=235.23)
print(jpy_value_rounded)

jpy_value_unrounded = convert_currency(
    jpy_exchange_rate, amount=235.23, round_result=False
)
print(jpy_value_unrounded)
