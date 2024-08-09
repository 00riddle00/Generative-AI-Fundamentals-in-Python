import json

exchange_rate_map = {"EUR": 0.927, "USD": 1, "CAD": 1.33, "JPY": 139.9, "GBP": 0.794}
print(type(exchange_rate_map))

exchange_rate_map_str = json.dumps(exchange_rate_map)
print(exchange_rate_map_str)
print(type(exchange_rate_map_str))
