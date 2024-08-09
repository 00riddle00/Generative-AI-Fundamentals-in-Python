import requests


def find_largest_exchange_rate(exchange_rates):
    largest_rate = 0
    largest_rate_country = ""
    for currency_code, rate in exchange_rates.items():
        if rate > largest_rate:
            largest_rate = rate
            largest_rate_country = currency_code
    print(largest_rate_country, largest_rate)
    return largest_rate


# Make API request to get the exchange rates
response = requests.get("https://api.exchangerate-api.com/v4/latest/usd")
api_exchange_rates = response.json().get("rates")

result = find_largest_exchange_rate(api_exchange_rates)
print(result)
