import re

applied_codes = [
    "P-49382",
    "X-21341",
    "P-2827",
    "A-45221",
    "S-420349",
    "M-89321",
    "S-98277",
    "D-21312",
    "P-73821",
    "T-73819",
    "Z-29381",
    "S23498",
    "R-23789",
    "P23123",
    "L-21391",
    "S-23812",
    "W-84321",
    "P-98123",
    "Q-34821",
    "S-39482",
]

seasonal_promotional_count = 0

pattern = re.compile(r"[SP]-\d+")

for code in applied_codes:
    match = re.search(pattern, code)
    if match:
        seasonal_promotional_count += 1
        print(match.group())

print(seasonal_promotional_count)
