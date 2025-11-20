#rock paper scissors game
import random 

emojis = {"r": "👊", "p": "📃", "s": "✂️"}
choices = tuple(emojis.keys())

def get_user_choice():
    """Get and validate user's choice"""
    while True:
        user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        print("Invalid choice!")

def get_computer_choice():
    """Get computer's random choice"""
    return random.choice(choices)

def display_choices(user_choice, computer_choice):
    """Display both player choices with emojis"""
    print(f"Your choice: {emojis[user_choice]}")
    print(f"Computer choice: {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    """Determine and display the winner"""
    if user_choice == computer_choice:
        print("It's a tie!🤝")
    elif (
        (user_choice == "s" and computer_choice == "p") or 
        (user_choice == "r" and computer_choice == "s") or 
        (user_choice == "p" and computer_choice == "r")):
        print("You win😎")
    else:
        print("You lose😔")

def ask_continue():
    """Ask if user wants to continue playing"""
    should_continue = input("Continue? (y/n): ").lower()
    return should_continue != "n"

def play_game():
    """Main game loop"""
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)
        
        if not ask_continue():
            print("Thank you for playing!")
            break

# Start the game
play_game()