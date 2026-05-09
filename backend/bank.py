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

    pin = input("Set 4-digit PIN: ")

    data[name] = {
    "pin": pin,
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

    data = load_data()

    # STEP 1: Check account existence
    if name not in data:
        print("❌ Account not found!")
        return

    # STEP 2: Ask PIN only if account exists
    pin = input("Enter PIN: ")

    # STEP 3: Verify PIN
    if data[name]["pin"] != pin:
        print("❌ Incorrect PIN!")
        return

    # STEP 4: Ask amount only after successful login
    amount = int(input("Enter amount: "))

    # STEP 5: Check balance
    if data[name]["balance"] >= amount:

        data[name]["balance"] -= amount

        data[name]["transactions"].append(
            f"Withdrew {amount}"
        )

        save_data(data)

        print("🏧 Withdrawal successful!")

    else:
        print("❌ Insufficient balance!") 

def check_balance():

    name = input("Enter name: ")

    data = load_data()

    # STEP 1: Check account existence
    if name not in data:
        print("❌ Account not found!")
        return

    # STEP 2: Ask PIN
    pin = input("Enter PIN: ")

    # STEP 3: Verify PIN
    if data[name]["pin"] != pin:
        print("❌ Incorrect PIN!")
        return

    # STEP 4: Show balance
    print(f"💰 Current Balance: ₹{data[name]['balance']}")
    
def history():

    name = input("Enter name: ")

    data = load_data()

    # STEP 1: Check account existence
    if name not in data:
        print("❌ Account not found!")
        return

    # STEP 2: Ask PIN
    pin = input("Enter PIN: ")

    # STEP 3: Verify PIN
    if data[name]["pin"] != pin:
        print("❌ Incorrect PIN!")
        return

    # STEP 4: Show transactions
    print("\n📜 Transaction History:")

    for t in data[name]["transactions"]:
        print("-", t)

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