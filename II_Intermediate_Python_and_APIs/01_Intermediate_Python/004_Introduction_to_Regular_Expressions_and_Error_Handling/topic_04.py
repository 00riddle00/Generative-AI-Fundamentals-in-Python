import re

# The list of emails we want to verify
phone_numbers = ["123-555-7890", "9875553210", "123-4567-89", "123-456-78", "156-7890"]

pattern = r"\d{3}-?\d{3}-?\d{4}"
verified_numbers = []

for number in phone_numbers:
    if re.fullmatch(pattern, number):
        verified_numbers.append(number)

print(verified_numbers)
