import re

# The list of phone numbers we want to verify
phone_numbers = ["123-555-7890", "9875553210", "123-4567-89", "123-456-78", "156-7890"]

# Regex pattern
pattern = r"[0-9]{3}-?[0-9]{3}-?[0-9]{4}"

validated_numbers = []


def validate_phone_number(phone_number):
    if not re.match(pattern, phone_number):
        raise ValueError("Invalid phone number.")


for number in phone_numbers:
    try:
        validate_phone_number(number)
        validated_numbers.append(number)
    except ValueError as e:
        print(e)

print(validated_numbers)
