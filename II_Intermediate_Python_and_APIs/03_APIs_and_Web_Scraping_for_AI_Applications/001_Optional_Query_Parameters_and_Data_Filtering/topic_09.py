import requests
import json

parameters = {
    "filter_by": "region=Europe & Central Asia,income_group=Upper middle income",
    "limit": 5,
    "offset": 0,
}

response = requests.get(
    "https://api-server.dataquest.io/economic_data/countries", params=parameters
)
data_combined_str = response.json()
data_combined = json.loads(data_combined_str)

for record in data_combined:
    country_name = record.get("table_name")
    print(country_name)
