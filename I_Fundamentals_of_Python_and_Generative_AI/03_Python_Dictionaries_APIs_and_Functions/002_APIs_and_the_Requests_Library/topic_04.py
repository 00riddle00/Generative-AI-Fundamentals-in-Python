import requests

currencies = ["EGP", "GMD", "CLP"]
base_url = "https://api.exchangerate-api.com/v4/latest/"

for currency_code in currencies:
    url = base_url + currency_code
    response = requests.get(url)
    response = response.json()
    print(response["rates"]["USD"])
