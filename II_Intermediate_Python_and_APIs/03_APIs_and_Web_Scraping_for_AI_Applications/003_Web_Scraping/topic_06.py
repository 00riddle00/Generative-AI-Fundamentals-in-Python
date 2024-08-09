import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException, HTTPError

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

try:
    response = requests.get(url)
    response.raise_for_status()
except RequestException as e:
    print(f"There was an issue with your request: {e}")
except HTTPError as e:
    print(f"HTTP error occurred: {e}")


soup = BeautifulSoup(response.text, "html.parser")
td_elements = soup.select("tr td")
td_elements = td_elements[13:]

population_list = []

for i in range(len(td_elements)):
    if i % 7 == 2:
        population = td_elements[i].text
        population_list.append(population)

print(population_list[:10])
