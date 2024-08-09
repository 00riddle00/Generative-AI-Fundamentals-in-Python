import base64
import requests

username = "dq"
password = "bad_password"

encoded_credentials = base64.b64encode(f"{username}:{password}".encode()).decode()

headers = {"Authorization": f"Basic {encoded_credentials}"}

url = "https://api-server.dataquest.io/private/economic_data/historical_data"

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
