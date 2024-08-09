import json

opened_file = open("currency_rates.json")
currency_rates = json.load(opened_file)
opened_file.close()
print(currency_rates)
