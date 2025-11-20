# number_guessing_game.py
import random

generated_number = random.randint(1, 100)  # generating random number between 1 to 100

print("Welcome to the Number Guessing Game!")
# Loop to continue guessing until the user guesses correctly
while True:
    try:
        guess_number = int(input("Guess the number (1-100): "))

        if guess_number < 1 or guess_number > 100:
            print("Invalid Number")
            continue

        if guess_number == generated_number:
            print("Well done")
            break
        elif guess_number < generated_number:
            print("Too low")
        else:
            print("Too high")

    # handling non-integer inputs
    except ValueError:
        print("Invalid input. Please enter a number")
