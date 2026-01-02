import json

FILE = "passwords.json"

# Load existing passwords or create an empty file
def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save data back to the file
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_password():
    account = input("Account name: ")
    password = input("Password: ")

    data = load_data()
    data[account] = password
    save_data(data)
    print("Saved!")

def view_passwords():
    data = load_data()
    if not data:
        print("No passwords saved.")
        return

    for account, password in data.items():
        print(f"{account}: {password}")

def search_password():
    account = input("Enter account to search: ")
    data = load_data()

    if account in data:
        print(f"Password: {data[account]}")
    else:
        print("Account not found.")

def main():
    while True:
        print("\n--- Password Manager ---")
        print("1. Add password")
        print("2. View all")
        print("3. Search password")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

main()
