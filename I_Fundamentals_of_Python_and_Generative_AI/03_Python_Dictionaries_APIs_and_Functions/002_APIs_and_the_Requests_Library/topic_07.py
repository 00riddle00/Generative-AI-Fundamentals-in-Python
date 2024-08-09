import requests

currencies = ["EGP", "GMD", "CLP"]
base_url = "https://api.exchangerate-api.com/v4/latest/"

for currency_code in currencies:
    url = f"{base_url}{currency_code}"
    response = requests.get(url)
    response = response.json()
    print(f"1 {currency_code} is equal to {response['rates']['USD']} USD")
