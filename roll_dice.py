# creating dice game
import random

print("Welcome to the Dice Rolling Simulator!")
# Loop to continue rolling the dice until the user decides to stop
while True:
    choice = input("Roll the dice(y/n): ").lower()
    if choice == "y":
        dice1 = random.randint(
            1, 6
        )  # generating random number between 1 to 6 for first dice
        dice2 = random.randint(
            1, 6
        )  # generating random number between 1 to 6 for second dice
        print(f" you rolled a {dice1} and a {dice2}")

    elif choice == "n":
        print("Thank you for playing. ")
        break  # Exit the loop and end the game

    else:
        print("Invalid choice!")
