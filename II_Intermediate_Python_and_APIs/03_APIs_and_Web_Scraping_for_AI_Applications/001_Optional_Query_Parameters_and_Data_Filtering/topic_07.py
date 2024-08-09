import requests
import json

parameters = {"limit": 10, "offset": 0}

response = requests.get(
    "https://api-server.dataquest.io/economic_data/indicators", params=parameters
)
indicator_page_str = response.json()
indicator_page = json.loads(indicator_page_str)

indicator_len_records = len(indicator_page)
fourth_indicator_name = indicator_page[3].get("indicator_name", [])

print(indicator_len_records)
print(fourth_indicator_name)
