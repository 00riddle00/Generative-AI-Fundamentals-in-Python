import requests
import json

parameters = {"limit": 50, "offset": 0}

response = requests.get(
    "https://api-server.dataquest.io/economic_data/indicators", params=parameters
)
data_str = response.json()
data_page_1 = json.loads(data_str)

print(parameters["limit"])
print(data_page_1[0]["topic"])

parameters["offset"] = 50
response = requests.get(
    "https://api-server.dataquest.io/economic_data/indicators", params=parameters
)
data_str = response.json()
data_page_2 = json.loads(data_str)
print(data_page_2[0]["topic"])
