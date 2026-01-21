import hashlib
import os

USERS_FILE = "users.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    print("\n=== REGISTRATION ===")
    username = input("Enter username: ")
    
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            for line in f:
                stored_user = line.split(':')[0]
                if stored_user == username:
                    print("Username already exists!")
                    return
    
    password = input("Enter password: ")
    hashed_pw = hash_password(password)
    
    with open(USERS_FILE, 'a') as f:
        f.write(f"{username}:{hashed_pw}\n")
    
    print("Registration successful!")


def login():
    print("\n=== LOGIN ===")
    username = input("Enter username: ")
    
    user_found = False
    stored_hash = None
    
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            for line in f:
                stored_user, stored_hash = line.strip().split(':')
                if stored_user == username:
                    user_found = True
                    break
    
    if not user_found:
        print("Username not found!")
        return
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        password = input("Enter password: ")
        hashed_input = hash_password(password)
        
        if hashed_input == stored_hash:
            print(f"\nLogin successful! Welcome, {username}!")
            return
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Incorrect password. {remaining} attempt(s) remaining.")
            else:
                print("Account locked due to too many failed attempts!")


def main():
    while True:
        print("\n" + "="*40)
        print("SIMPLE LOGIN SYSTEM")
        print("="*40)
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ")
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
