import requests

currency_codes = ["cad", "abc"]
base_url = "https://api.exchangerate-api.com/v4/latest/"

for currency_code in currency_codes:
    url = f"{base_url}{currency_code}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        print("Request was successful!")
    elif response.status_code == 404:
        print("Endpoint not found!")
    else:
        print("An error occurred!")
