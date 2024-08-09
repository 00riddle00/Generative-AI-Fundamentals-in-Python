import requests


def convert_amount(original_currency_rate, amount):
    converted_amount = amount * original_currency_rate
    return converted_amount


def get_exchange_rate(target_currency, original_currency):
    # Make API request to get the exchange rate
    url = "https://api.exchangerate-api.com/v4/latest/" + original_currency
    response = requests.get(url)
    data = response.json()

    # Extract the exchange rate for the desired currency
    exchange_rate = data["rates"][target_currency]

    return exchange_rate


original_currency = "USD"
target_currency = "ZMW"
amount = 100

converted_amount = convert_amount(
    get_exchange_rate(target_currency, original_currency), amount
)
print(converted_amount)
