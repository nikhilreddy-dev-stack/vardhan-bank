# 🏦 Python Banking System

A secure command-line banking system built using Python and JSON storage.

This project simulates core banking operations such as account creation, login authentication, deposits, withdrawals, money transfers, transaction history, and temporary account locking after multiple failed login attempts.

---

# ✨ Features

## 🔐 Authentication & Security

* Secure login using Account Number + PIN
* Hidden PIN input using `getpass`
* Automatic account lock after 3 wrong PIN attempts
* Temporary 30-second lock system

## 🏦 Banking Operations

* Create account with randomly generated account number
* Deposit money
* Withdraw money
* Transfer money between accounts
* Check account balance
* View transaction history

## 📜 Smart Transaction System

* Timestamped transaction records
* Transfer sender/receiver details stored in history
* Persistent storage using JSON database

---

# 🧠 Concepts Used

This project demonstrates several important backend development concepts:

* Functions
* JSON file handling
* Authentication systems
* Session-based login flow
* Nested dictionaries
* Random account number generation
* Time handling with `datetime`
* Account locking system
* Data persistence
* Input validation

---

# 🛠️ Technologies Used

* Python 3
* JSON
* datetime module
* random module
* getpass module

---

# 📂 Project Structure

```bash
banking-system/
│
├── bank.py
├── bank.json
└── README.md
```

---

# 🖥️ Main Menu

```text
====== BANKING SYSTEM ======
1. Create Account
2. Login
3. Exit
```

---

# 👤 User Dashboard

```text
1. Deposit
2. Withdraw
3. Check Balance
4. Transaction History
5. Transfer Money
6. Logout
```

---

# 🔒 Account Locking System

After 3 incorrect PIN attempts:

```text
🔒 Too many wrong attempts! Account locked for 30 seconds.
```

The account automatically unlocks after 30 seconds.

---

# 📜 Example Transaction History

```text
[2026-05-10 12:01:14 AM] Deposited ₹5000
[2026-05-10 12:03:28 AM] Withdrew ₹700
[2026-05-10 12:04:10 AM] Transferred ₹1000 to Rahul (48392017)
```

---

# 🔥 Future Improvements

Planned upgrades:

* Flask web version
* SQLite/MySQL database
* OTP verification system
* Email notifications
* Debit card generation
* Mini statement download
* GUI dashboard
* Admin panel

---
