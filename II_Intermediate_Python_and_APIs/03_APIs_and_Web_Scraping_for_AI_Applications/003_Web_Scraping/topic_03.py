import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", {"class": "wikitable"})
rows = table.find_all("tr")

top_100_countries = rows[2:102]

for country in top_100_countries:
    cols = country.find_all("td")
    cols = [col.text.strip() for col in cols]
    print(cols)
