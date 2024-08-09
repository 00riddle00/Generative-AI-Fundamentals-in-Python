import requests

url = "https://api-server.dataquest.io/private/historical_data"

response = requests.get(url)
print(response.status_code)
