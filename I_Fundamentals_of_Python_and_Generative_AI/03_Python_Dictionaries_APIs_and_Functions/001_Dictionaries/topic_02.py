conversion_rates = [["EUR", 0.85], ["GBP", 0.72], ["JPY", 109.35], ["CAD", 1.21]]

currency_rates = {rate[0]: rate[1] for rate in conversion_rates}
print(currency_rates)
