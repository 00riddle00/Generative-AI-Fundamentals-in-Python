import base64
import requests

username = "dq"
password = "test"

encoded_credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
headers = {"Authorization": f"Basic {encoded_credentials}"}

url = "https://api-server.dataquest.io/private/economic_data"
endpoint = "/historical_data"
response = requests.get(url + endpoint, headers=headers)

print(response.status_code)

if response.status_code == 200:
    response_preview = response.text[:500]
