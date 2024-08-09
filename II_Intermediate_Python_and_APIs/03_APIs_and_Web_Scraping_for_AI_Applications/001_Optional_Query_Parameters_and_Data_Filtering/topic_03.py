import requests
import json

response = requests.get(
    "https://api-server.dataquest.io/economic_data/indicators?filter_by=topic=Health:%20Risk%20factors&filter_by=periodicity=Biennial"
)
topic_str = response.json()
topic = json.loads(topic_str)

for indicator in topic:
    print(indicator["series_code"])
    print(indicator["indicator_name"])
