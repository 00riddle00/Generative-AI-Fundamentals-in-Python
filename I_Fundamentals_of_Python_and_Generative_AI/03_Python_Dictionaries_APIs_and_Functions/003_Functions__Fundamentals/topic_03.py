import requests


def convert_amount(exchange_rate):
    """This function multiples the exchange rate by the amount to convert"""
    amount = 500
    converted_amount = exchange_rate * amount
    return converted_amount


# Make API request to get the exchange rates
response = requests.get("https://api.exchangerate-api.com/v4/latest/usd")
exchange_rates = response.json().get("rates")

jpy_value = convert_amount(exchange_rates["JPY"])
clp_value = convert_amount(exchange_rates["CLP"])

print(jpy_value)
print(clp_value)
