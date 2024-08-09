import requests

response = requests.get(
    "https://api-server.dataquest.io/economic_data/countries?filter_by=region=South%20Asia"
)
region_south_asia = response.json()
print(region_south_asia)
