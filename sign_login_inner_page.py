import re
import csv
import os
import random
import string

def sign():
    print("====== Registration ======")
    
    # Read existing users first
    existing_users = set()
    existing_emails = set()
    
    if os.path.exists("users.csv") and os.path.getsize("users.csv") > 0:
        with open("users.csv", "r") as file:
            reader = csv.DictReader(file)
            for user in reader:
                existing_users.add(user['userName'])
                existing_emails.add(user['email'])
    
    with open("users.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["email", "password", "userName"])
        
        # Write header if file is new or empty
        if not os.path.exists("users.csv") or os.path.getsize("users.csv") == 0:
            writer.writeheader()
        
        # Email validation loop (only once)
        while True:
            email = input("Enter your email: ").strip()
            
            # Check if email already exists
            if email in existing_emails:
                print("Email already registered. Please login instead.")
                continue
            
            if re.search(r"^\w+@(\w+\.)?\w+(\.edu|\.com)$", email, re.IGNORECASE):
                print("Valid email ✓")
                break  # Exit email loop once valid
            else:
                print("Invalid email format. Please use format: example@domain.com or example@domain.edu")
        
        # Password option selection
        print("\n--- Password Setup ---")
        print("1. Create your own password")
        print("2. Generate a secure password automatically")
        
        password_choice = None
        while password_choice not in ["1", "2"]:
            password_choice = input("Choose option (1 or 2): ").strip()
            if password_choice not in ["1", "2"]:
                print("Invalid choice. Please enter 1 or 2.")
        
        # Password validation loop (separate)
        if password_choice == "2":
            # Auto-generate secure password
            password = ''.join(random.choices(
                string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%&*", 
                k=12
            ))
            print("\n" + "=" * 50)
            print("✓ Your secure password has been generated!")
            print(f"Password: {password}")
            print("=" * 50)
            print("⚠️ IMPORTANT: Save this password somewhere safe!")
            print("You'll need it to login.")
            print("=" * 50)
            input("Press Enter after saving your password...")
            
            # Generate unique username
            base_username = email.split("@")[0]
            userName = base_username + ''.join(random.choices(string.ascii_letters + string.digits, k=2))
            
            # Ensure uniqueness
            while userName in existing_users:
                userName = base_username + ''.join(random.choices(string.ascii_letters + string.digits, k=2))
            
            writer.writerow({"email": email, "password": password, "userName": userName})
            print("\n✓ Registration successful!")
            print(f"Welcome, {userName}!")
            print(f"Your username is: {userName}")
            print("Please remember your username for login.\n")
        
        else:
            # Manual password entry
            while True:
                password = input("Enter your password: ")
                
                # Password strength check
                if len(password) < 6:
                    print("Password must be at least 6 characters long.")
                    continue
                
                confirm_password = input("Confirm your password: ")

                if password == confirm_password:
                    print("Password confirmed ✓")
                    
                    # Generate unique username
                    base_username = email.split("@")[0]
                    userName = base_username + ''.join(random.choices(string.ascii_letters + string.digits, k=2))
                    
                    # Ensure uniqueness
                    while userName in existing_users:
                        userName = base_username + ''.join(random.choices(string.ascii_letters + string.digits, k=2))
                    
                    writer.writerow({"email": email, "password": password, "userName": userName})
                    print("\n✓ Registration successful!")
                    print(f"Welcome, {userName}!")
                    print(f"Your username is: {userName}")
                    print("Please remember your username for login.\n")
                    break
                else:
                    print("Passwords do not match. Please try again.")

def login():
    print("====== Login ======")
    
    if not os.path.exists("users.csv") or os.path.getsize("users.csv") == 0:
        print("No users registered yet. Please register first.")
        return
    
    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        users = list(reader)
        
        attempts = 0
        max_attempts = 3
        
        while attempts < max_attempts:
            userName = input("Enter your username: ").strip()
            password = input("Enter your password: ")
            
            user_found = False
            for user in users:
                if user['userName'] == userName and user['password'] == password:
                    print("\n✓ Login successful!")
                    print(f"Welcome back, {user['userName']}!")
                    print(f"Email: {user['email']}\n")
                    user_found = True
                    break
            
            if user_found:
                break
            else:
                attempts += 1
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"Invalid username or password. {remaining} attempt(s) remaining.")
                else:
                    print("Maximum attempts reached. Please try again later.")

def main():
    # Create file if it doesn't exist
    if not os.path.exists("users.csv"):
        open("users.csv", "w").close()

    print("=" * 40)
    print("    USER AUTHENTICATION SYSTEM")
    print("=" * 40)
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("=" * 40)

    while True:
        try:
            choice = int(input("Choose an option (1-3): "))
            
            if choice == 1:
                sign()
                break
            elif choice == 2:
                login()
                break
            elif choice == 3:
                print("Exiting... Goodbye!")
                exit()
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
            
        except ValueError:
            print("Invalid input. Please enter a number (1-3).")

if __name__ == "__main__":
    main()