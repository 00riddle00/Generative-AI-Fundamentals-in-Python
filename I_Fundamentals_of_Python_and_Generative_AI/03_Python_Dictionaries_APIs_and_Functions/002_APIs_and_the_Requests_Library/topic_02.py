import requests

endpoint_url = "https://api.exchangerate-api.com/v4/latest/cad"

response = requests.get(endpoint_url)

print(response, type(response))
