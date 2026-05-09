import json

FILE = "bank.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def create_account():
    name = input("Enter your name: ")
    data = load_data()

    if name in data:
        print("Account already exists!")
        return

    data[name] = {
        "balance": 0,
        "transactions": []
    }

    save_data(data)
    print("✅ Account created!")

def deposit():
    name = input("Enter name: ")
    amount = int(input("Enter amount: "))
    data = load_data()

    if name in data:
        data[name]["balance"] += amount
        data[name]["transactions"].append(f"Deposited {amount}")
        save_data(data)
        print("💰 Deposited!")
    else:
        print("Account not found!")

def withdraw():
    name = input("Enter name: ")
    amount = int(input("Enter amount: "))
    data = load_data()

    if name in data:
        if data[name]["balance"] >= amount:
            data[name]["balance"] -= amount
            data[name]["transactions"].append(f"Withdrew {amount}")
            save_data(data)
            print("🏧 Withdrawn!")
        else:
            print("❌ Insufficient balance!")
    else:
        print("Account not found!")

def check_balance():
    name = input("Enter name: ")
    data = load_data()

    if name in data:
        print("Balance:", data[name]["balance"])
    else:
        print("Account not found!")

def history():
    name = input("Enter name: ")
    data = load_data()

    if name in data:
        print("\nTransactions:")
        for t in data[name]["transactions"]:
            print("-", t)
    else:
        print("Account not found!")

while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Balance\n5. History\n6. Exit")
    choice = input("Choose: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        history()
    else:
        break