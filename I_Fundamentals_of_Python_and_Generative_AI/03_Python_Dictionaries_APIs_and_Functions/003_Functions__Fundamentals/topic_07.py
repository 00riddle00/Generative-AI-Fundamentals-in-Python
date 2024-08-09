import json
import requests


def convert_amount(original_currency_rate, amount):
    converted_amount = amount / original_currency_rate
    return converted_amount


def calculate_total_purchases_in_currency(orders, target_currency):
    api_exchange_rates = requests.get(base_api_url + target_currency).json()
    total_purchases_in_currency = 0
    for order in orders:
        purchase_total = orders[order]["purchase_total"]
        currency = orders[order]["currency"]
        exchange_rate = api_exchange_rates["rates"][currency]
        total_purchases_in_currency += convert_amount(exchange_rate, purchase_total)
    return total_purchases_in_currency


# Make API request to get the exchange rates
base_api_url = "https://api.exchangerate-api.com/v4/latest/"

opened_file = open("global_daily_sales.json")
orders = json.load(opened_file)
opened_file.close()

usd_total = calculate_total_purchases_in_currency(orders, "USD")
jpy_total = calculate_total_purchases_in_currency(orders, "JPY")
cad_total = calculate_total_purchases_in_currency(orders, "CAD")
awg_total = calculate_total_purchases_in_currency(orders, "AWG")

print(usd_total)
print(jpy_total)
print(cad_total)
print(awg_total)
