currency_rates = {"EUR": 0.85, "GBP": 0.72, "JPY": 109.35, "CAD": 1.21}

removed_gbp_value = currency_rates.pop("GBP")
removed_cad_value = currency_rates.pop("CAD")
print(removed_gbp_value)
print(removed_cad_value)
print(currency_rates)

currency_rates.clear()
print(currency_rates)
