import requests


def convert_amount(exchange_rate, amount):
    converted_amount = exchange_rate * amount
    return converted_amount


# Make API request to get the exchange rates
response = requests.get("https://api.exchangerate-api.com/v4/latest/usd")
api_exchange_rates = response.json().get("rates")

eur_converted_1 = convert_amount(api_exchange_rates.get("EUR"), 500)
eur_converted_2 = convert_amount(api_exchange_rates.get("EUR"), 100)
ttd_converted = convert_amount(api_exchange_rates.get("TTD"), 66.70)
shp_converted = convert_amount(api_exchange_rates.get("SHP"), 334.50)

print(eur_converted_1, eur_converted_2, ttd_converted, shp_converted)
