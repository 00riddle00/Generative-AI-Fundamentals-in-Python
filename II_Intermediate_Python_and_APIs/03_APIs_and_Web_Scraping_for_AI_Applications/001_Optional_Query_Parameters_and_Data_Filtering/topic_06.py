import requests
import json

parameters = {"limit": 10, "offset": 0}
response = requests.get(
    "https://api-server.dataquest.io/economic_data/countries", params=parameters
)
data_with_pagination = json.loads(response.json())
print(len(data_with_pagination))
