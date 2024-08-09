import random

number_to_guess = 0
num_guesses = 5

number_to_guess = random.randint(1, 10)

while num_guesses > 0:
    print("Guess a number between 1 and 10!")
    response = random.randint(1, 10)
    response_str = str(response)
    print("You guessed: " + response_str)
    num_guesses -= 1
