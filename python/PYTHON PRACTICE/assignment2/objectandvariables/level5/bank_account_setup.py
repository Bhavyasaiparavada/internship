# Question 5: Create a BankAccount class using __init__() with account holder, account number, and initial balance.

class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0):
        """Initialize bank account attributes"""
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = []
        
        if initial_balance > 0:
            self.transaction_history.append(f"Initial Deposit: ${initial_balance:,.2f}")
    
    def deposit(self, amount):
        """Deposit money to account"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount:,.2f}")
            print(f"✓ Deposit successful!")
            print(f"  Amount: ${amount:,.2f}")
            print(f"  New Balance: ${self.balance:,.2f}\n")
        else:
            print("Error: Deposit amount must be positive!\n")
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrawal: -${amount:,.2f}")
                print(f"✓ Withdrawal successful!")
                print(f"  Amount: ${amount:,.2f}")
                print(f"  Remaining Balance: ${self.balance:,.2f}\n")
            else:
                print(f"Error: Insufficient balance!")
                print(f"  Available: ${self.balance:,.2f}\n")
        else:
            print("Error: Withdrawal amount must be positive!\n")
    
    def display_account_info(self):
        """Display account information"""
        print(f"\n{'='*50}")
        print(f"Account Information:")
        print(f"{'='*50}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance:,.2f}")
        print(f"{'='*50}\n")
    
    def display_transaction_history(self):
        """Display transaction history"""
        print(f"\nTransaction History for {self.account_holder}")
        print(f"Account: {self.account_number}")
        print(f"{'-'*50}")
        for transaction in self.transaction_history:
            print(f"  {transaction}")
        print(f"{'-'*50}")
        print(f"Current Balance: ${self.balance:,.2f}\n")
    
    def transfer(self, recipient_account, amount):
        """Transfer money to another account"""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                recipient_account.balance += amount
                self.transaction_history.append(f"Transfer to {recipient_account.account_number}: -${amount:,.2f}")
                recipient_account.transaction_history.append(f"Transfer from {self.account_number}: +${amount:,.2f}")
                print(f"✓ Transfer successful!")
                print(f"  From: {self.account_holder} ({self.account_number})")
                print(f"  To: {recipient_account.account_holder} ({recipient_account.account_number})")
                print(f"  Amount: ${amount:,.2f}\n")
            else:
                print(f"Error: Insufficient balance for transfer!\n")
        else:
            print("Error: Transfer amount must be positive!\n")


# Create bank account objects using __init__()
print("BANK ACCOUNT MANAGEMENT SYSTEM\n")

account1 = BankAccount("Alice Johnson", "ACC001", 5000)
account2 = BankAccount("Bob Smith", "ACC002", 3000)
account3 = BankAccount("Charlie Brown", "ACC003", 7500)

# Display account information
account1.display_account_info()
account2.display_account_info()
account3.display_account_info()

# Perform transactions
print("TRANSACTIONS")
print("=" * 50)

print("\nAccount 1 Transactions:")
account1.deposit(1000)
account1.withdraw(500)
account1.deposit(2000)

print("Account 2 Transactions:")
account2.withdraw(800)
account2.deposit(2000)

print("Account 3 Transactions:")
account3.withdraw(2000)
account3.deposit(3000)

# Transfer money
print("MONEY TRANSFER")
print("=" * 50 + "\n")
account1.transfer(account2, 1000)
account2.transfer(account3, 500)

# Display final account information
print("\nFINAL ACCOUNT INFORMATION")
print("=" * 50)
account1.display_account_info()
account2.display_account_info()
account3.display_account_info()

# Display transaction history
print("\nTRANSACTION HISTORY")
print("=" * 50)
account1.display_transaction_history()
account2.display_transaction_history()
account3.display_transaction_history()
