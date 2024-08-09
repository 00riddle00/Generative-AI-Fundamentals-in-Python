import requests

# Make API request to get the exchange rates
response = requests.get("https://api.exchangerate-api.com/v4/latest/usd")
exchange_rates = response.json().get("rates")

kyd_value = exchange_rates.get("KYD")
print(kyd_value)
