import json

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
# CREATE ACCOUNT
# =========================
def create_account():

    data = load_data()

    name = input("Enter username: ")

    if name in data:
        print("❌ Account already exists!")
        return

    pin = input("Set 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("❌ PIN must be exactly 4 digits!")
        return

    data[name] = {
        "pin": pin,
        "balance": 0,
        "transactions": []
    }

    save_data(data)

    print("✅ Account created successfully!")


# =========================
# LOGIN
# =========================
def login():

    data = load_data()

    name = input("Enter username: ")

    if name not in data:
        print("❌ Account not found!")
        return None

    pin = input("Enter PIN: ")

    if data[name]["pin"] != pin:
        print("❌ Incorrect PIN!")
        return None

    print(f"\n✅ Welcome, {name}!")

    return name


# =========================
# DEPOSIT
# =========================
def deposit(current_user):

    data = load_data()

    amount = int(input("Enter deposit amount: "))

    if amount <= 0:
        print("❌ Invalid amount!")
        return

    data[current_user]["balance"] += amount

    data[current_user]["transactions"].append(
        f"Deposited ₹{amount}"
    )

    save_data(data)

    print("💰 Deposit successful!")


# =========================
# WITHDRAW
# =========================
def withdraw(current_user):

    data = load_data()

    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("❌ Invalid amount!")
        return

    if data[current_user]["balance"] < amount:
        print("❌ Insufficient balance!")
        return

    # Final confirmation PIN
    pin = input("Enter PIN to confirm withdrawal: ")

    if data[current_user]["pin"] != pin:
        print("❌ Incorrect PIN!")
        return

    data[current_user]["balance"] -= amount

    data[current_user]["transactions"].append(
        f"Withdrew ₹{amount}"
    )

    save_data(data)

    print("🏧 Withdrawal successful!")


# =========================
# CHECK BALANCE
# =========================
def check_balance(current_user):

    data = load_data()

    print(f"\n💰 Current Balance: ₹{data[current_user]['balance']}")


# =========================
# TRANSACTION HISTORY
# =========================
def history(current_user):

    data = load_data()

    print("\n📜 Transaction History:")

    if len(data[current_user]["transactions"]) == 0:
        print("No transactions yet.")
        return

    for t in data[current_user]["transactions"]:
        print("-", t)


# =========================
# TRANSFER MONEY
# =========================
def transfer_money(current_user):

    data = load_data()

    receiver = input("Enter receiver username: ")

    if receiver not in data:
        print("❌ Receiver account not found!")
        return

    if receiver == current_user:
        print("❌ Cannot transfer to yourself!")
        return

    amount = int(input("Enter transfer amount: "))

    if amount <= 0:
        print("❌ Invalid amount!")
        return

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

    # Transaction logs
    data[current_user]["transactions"].append(
        f"Transferred ₹{amount} to {receiver}"
    )

    data[receiver]["transactions"].append(
        f"Received ₹{amount} from {current_user}"
    )

    save_data(data)

    print("✅ Transfer successful!")


# =========================
# USER DASHBOARD
# =========================
def user_dashboard(current_user):

    while True:

        print(f"\n====== {current_user.upper()} DASHBOARD ======")
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
            print(f"👋 Logged out from {current_user}")
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