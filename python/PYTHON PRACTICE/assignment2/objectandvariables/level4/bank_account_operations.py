# Question 6: Create a BankAccount class with methods deposit() and withdraw().

class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✓ Deposit Successful!")
            print(f"  Amount Deposited: ${amount:,.2f}")
            print(f"  Current Balance: ${self.balance:,.2f}\n")
        else:
            print("Error: Deposit amount must be positive!\n")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"✓ Withdrawal Successful!")
                print(f"  Amount Withdrawn: ${amount:,.2f}")
                print(f"  Current Balance: ${self.balance:,.2f}\n")
            else:
                print(f"Error: Insufficient balance! (Available: ${self.balance:,.2f})\n")
        else:
            print("Error: Withdrawal amount must be positive!\n")
    
    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance:,.2f}")
        print("-" * 40)
    
    def display_account_statement(self):
        print(f"\nAccount Statement for {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:,.2f}")
        print("-" * 40)


# Create bank account objects
account1 = BankAccount("Alice Johnson", "ACC001", 5000)
account2 = BankAccount("Bob Smith", "ACC002", 3000)
account3 = BankAccount("Charlie Brown", "ACC003", 7500)

# Display initial balances
print("Initial Account Balances:\n")
account1.display_balance()
account2.display_balance()
account3.display_balance()

# Perform transactions
print("\n--- Transactions ---\n")
print(f"Transaction 1 - {account1.account_holder}:")
account1.deposit(1000)
account1.withdraw(500)

print(f"Transaction 2 - {account2.account_holder}:")
account2.deposit(2000)
account2.withdraw(800)

print(f"Transaction 3 - {account3.account_holder}:")
account3.withdraw(2000)
account3.deposit(3000)

# Try invalid transaction
print(f"Transaction 4 - {account2.account_holder} (Attempt to withdraw more than balance):")
account2.withdraw(10000)

# Display final balances
print("\n--- Final Account Balances ---\n")
account1.display_account_statement()
account2.display_account_statement()
account3.display_account_statement()
