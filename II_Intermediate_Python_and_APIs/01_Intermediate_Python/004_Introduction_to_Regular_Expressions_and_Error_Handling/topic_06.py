user_input = "twenty"

try:
    number = int(user_input)
    print("You are purchasing a quantity of", number)
except ValueError:
    print("That's not a valid number!")
finally:
    print("Thank you!")
