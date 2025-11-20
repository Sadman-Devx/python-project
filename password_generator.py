# Password Generator: A tool that generates random, secure passwords based on user-defined criteria.
import random
import string
def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """Generate a random password based on specified criteria."""
    character_pool = ""
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter desired password length (default 12): ") or 12)
    use_upper = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
    use_lower = input("Include lowercase letters? (y/n, default y): ").lower() != 'n'
    use_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
    use_special = input("Include special characters? (y/n, default y): ").lower() != 'n'

    try:
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()

