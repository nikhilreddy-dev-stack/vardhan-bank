import json
import random
from datetime import datetime

FILE = "bank.json"


# =========================
# LOAD DATA
# =========================
def load_data():

    try:
        with open(FILE, "r") as f:
            return json.load(f)

    except:
        return {}


# =========================
# SAVE DATA
# =========================
def save_data(data):

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# =========================
# GENERATE ACCOUNT NUMBER
# =========================
def generate_account_number(data):

    while True:

        account_number = str(
            random.randint(10000000, 99999999)
        )

        # Ensure uniqueness
        if account_number not in data:
            return account_number


# =========================
# GET TIMESTAMP
# =========================
def get_timestamp():

    return datetime.now().strftime(
        "%Y-%m-%d %I:%M:%S %p"
    )


# =========================
# CREATE ACCOUNT
# =========================
def create_account():

    data = load_data()

    name = input("Enter your name: ")

    pin = input("Set 4-digit PIN: ")

    # PIN validation
    if len(pin) != 4 or not pin.isdigit():
        print("❌ PIN must be exactly 4 digits!")
        return

    # Generate unique account number
    account_number = generate_account_number(data)

    data[account_number] = {
        "name": name,
        "pin": pin,
        "balance": 0,
        "transactions": []
    }

    save_data(data)

    print("\n✅ Account created successfully!")
    print(f"🏦 Your Account Number: {account_number}")


# =========================
# LOGIN
# =========================
def login():

    data = load_data()

    account_number = input("Enter Account Number: ")

    # Check account existence
    if account_number not in data:
        print("❌ Account not found!")
        return None

    pin = input("Enter PIN: ")

    # Verify PIN
    if data[account_number]["pin"] != pin:
        print("❌ Incorrect PIN!")
        return None

    print(
        f"\n✅ Welcome, {data[account_number]['name']}!"
    )

    return account_number


# =========================
# DEPOSIT
# =========================
def deposit(current_user):

    data = load_data()

    amount = int(input("Enter deposit amount: "))

    # Validate amount
    if amount <= 0:
        print("❌ Invalid amount!")
        return

    data[current_user]["balance"] += amount

    data[current_user]["transactions"].append(
        f"[{get_timestamp()}] Deposited ₹{amount}"
    )

    save_data(data)

    print("💰 Deposit successful!")


# =========================
# WITHDRAW
# =========================
def withdraw(current_user):

    data = load_data()

    amount = int(input("Enter withdrawal amount: "))

    # Validate amount
    if amount <= 0:
        print("❌ Invalid amount!")
        return

    # Check balance
    if data[current_user]["balance"] < amount:
        print("❌ Insufficient balance!")
        return

    # Final PIN confirmation
    pin = input("Enter PIN to confirm withdrawal: ")

    if data[current_user]["pin"] != pin:
        print("❌ Incorrect PIN!")
        return

    data[current_user]["balance"] -= amount

    data[current_user]["transactions"].append(
        f"[{get_timestamp()}] Withdrew ₹{amount}"
    )

    save_data(data)

    print("🏧 Withdrawal successful!")


# =========================
# CHECK BALANCE
# =========================
def check_balance(current_user):

    data = load_data()

    print(
        f"\n💰 Current Balance: ₹{data[current_user]['balance']}"
    )


# =========================
# TRANSACTION HISTORY
# =========================
def history(current_user):

    data = load_data()

    print("\n📜 Transaction History:")

    if len(data[current_user]["transactions"]) == 0:
        print("No transactions yet.")
        return

    for transaction in data[current_user]["transactions"]:
        print("-", transaction)


# =========================
# TRANSFER MONEY
# =========================
def transfer_money(current_user):

    data = load_data()

    receiver = input(
        "Enter receiver account number: "
    )

    # Check receiver existence
    if receiver not in data:
        print("❌ Receiver account not found!")
        return

    # Prevent self transfer
    if receiver == current_user:
        print("❌ Cannot transfer to your own account!")
        return

    amount = int(input("Enter transfer amount: "))

    # Validate amount
    if amount <= 0:
        print("❌ Invalid amount!")
        return

    # Check balance
    if data[current_user]["balance"] < amount:
        print("❌ Insufficient balance!")
        return

    # Final PIN confirmation
    pin = input("Enter PIN to confirm transfer: ")

    if data[current_user]["pin"] != pin:
        print("❌ Incorrect PIN!")
        return

    # Transfer process
    data[current_user]["balance"] -= amount

    data[receiver]["balance"] += amount

    sender_name = data[current_user]["name"]
    receiver_name = data[receiver]["name"]

    # Sender transaction log
    data[current_user]["transactions"].append(
        f"[{get_timestamp()}] Transferred ₹{amount} to {receiver_name} ({receiver})"
    )

    # Receiver transaction log
    data[receiver]["transactions"].append(
        f"[{get_timestamp()}] Received ₹{amount} from {sender_name} ({current_user})"
    )

    save_data(data)

    print("✅ Transfer successful!")


# =========================
# USER DASHBOARD
# =========================
def user_dashboard(current_user):

    data = load_data()

    user_name = data[current_user]["name"]

    while True:

        print(
            f"\n====== {user_name.upper()}'S DASHBOARD ======"
        )

        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Transfer Money")
        print("6. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            deposit(current_user)

        elif choice == "2":
            withdraw(current_user)

        elif choice == "3":
            check_balance(current_user)

        elif choice == "4":
            history(current_user)

        elif choice == "5":
            transfer_money(current_user)

        elif choice == "6":
            print(f"👋 Logged out from {user_name}")
            break

        else:
            print("❌ Invalid choice!")


# =========================
# MAIN MENU
# =========================
while True:

    print("\n====== BANKING SYSTEM ======")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_account()

    elif choice == "2":

        current_user = login()

        # If login successful
        if current_user:
            user_dashboard(current_user)

    elif choice == "3":
        print("👋 Thank you for using the banking system!")
        break

    else:
        print("❌ Invalid choice!")