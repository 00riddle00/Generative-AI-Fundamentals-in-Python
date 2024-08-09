import requests
from bs4 import BeautifulSoup


def extract_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "wikitable"})
    rows = table.find_all("tr")

    data = []
    for row in rows:
        cols = row.find_all("td")
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    return data


population_data = extract_data(
    "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
)

print(population_data[:5])
