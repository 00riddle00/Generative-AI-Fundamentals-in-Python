import requests

endpoint_url = "https://api.exchangerate-api.com/v4/latest/gbp"

response = requests.get(endpoint_url)
response_dict = response.json()

print(type(response))
print(type(response_dict))

for key in response_dict:
    print(key, response_dict[key])
