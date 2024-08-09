import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"

payload = {"date": "2023-06-13"}
response = requests.post(url, json=payload)
response_dict = response.json()
print(response_dict)
