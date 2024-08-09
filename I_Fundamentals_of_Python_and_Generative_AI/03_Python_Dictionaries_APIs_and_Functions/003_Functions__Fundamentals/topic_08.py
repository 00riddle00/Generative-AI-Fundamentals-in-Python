import requests


def convert_amount(original_currency, target_currency, amount):
    url = "https://api.exchangerate-api.com/v4/latest/" + target_currency
    response = requests.get(url + target_currency)
    api_exchange_rates = response.json().get("rates")
    converted_amount = amount / api_exchange_rates[original_currency]
    return converted_amount


cad_to_usd1 = convert_amount(original_currency="CAD", target_currency="USD", amount=50)
cad_to_usd2 = convert_amount(target_currency="USD", original_currency="CAD", amount=50)
cad_to_usd3 = convert_amount("CAD", "USD", 50)
cad_to_usd4 = convert_amount("USD", "CAD", 50)

print(cad_to_usd1)
print(cad_to_usd2)
print(cad_to_usd3)
print(cad_to_usd4)
