import requests
import json

response = requests.get(
    "https://api-server.dataquest.io/economic_data/indicators?filter_by=indicator_period=Biennial"
)

invalid_data_str = response.json()
print(invalid_data_str)
