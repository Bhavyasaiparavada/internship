# Question 4: Create a BankAccount class with a method that accepts an amount and deposits it into the account.

class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0):
        """Initialize bank account"""
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []
        
        if initial_balance > 0:
            self.transactions.append(("Initial Deposit", initial_balance, self.balance))
    
    def deposit(self, amount):
        """
        Accept an amount and deposit it into the account
        Method accepts amount as parameter and updates balance
        """
        if amount <= 0:
            print(f"Error: Deposit amount must be positive!")
            return False
        
        self.balance += amount
        self.transactions.append(("Deposit", amount, self.balance))
        print(f"✓ Deposit Successful!")
        print(f"  Amount: ${amount:,.2f}")
        print(f"  New Balance: ${self.balance:,.2f}\n")
        return True
    
    def withdraw(self, amount):
        """Withdraw amount from account"""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive!")
            return False
        
        if amount > self.balance:
            print(f"Error: Insufficient balance!")
            print(f"  Available: ${self.balance:,.2f}\n")
            return False
        
        self.balance -= amount
        self.transactions.append(("Withdrawal", amount, self.balance))
        print(f"✓ Withdrawal Successful!")
        print(f"  Amount: ${amount:,.2f}")
        print(f"  Remaining Balance: ${self.balance:,.2f}\n")
        return True
    
    def get_balance(self):
        """Get current balance"""
        return self.balance
    
    def display_balance(self):
        """Display account balance"""
        print(f"\nAccount: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance:,.2f}\n")
    
    def display_transaction_history(self):
        """Display all transactions"""
        print(f"\nTransaction History - {self.account_holder}")
        print(f"Account: {self.account_number}")
        print("=" * 60)
        print(f"{'Type':<15} {'Amount':<15} {'Balance After':<20}")
        print("-" * 60)
        
        for trans_type, amount, balance in self.transactions:
            print(f"{trans_type:<15} ${amount:>12,.2f}  ${balance:>16,.2f}")
        
        print("-" * 60)
        print(f"{'Current Balance':<15} ${self.balance:>12,.2f}\n")
    
    def calculate_interest(self, annual_rate):
        """Calculate interest based on annual rate"""
        interest = (self.balance * annual_rate) / 100
        return interest
    
    def apply_interest(self, annual_rate):
        """Apply interest to account"""
        interest = self.calculate_interest(annual_rate)
        self.balance += interest
        self.transactions.append(("Interest", interest, self.balance))
        print(f"✓ Interest Applied!")
        print(f"  Rate: {annual_rate}%")
        print(f"  Interest Amount: ${interest:,.2f}")
        print(f"  New Balance: ${self.balance:,.2f}\n")


# Create bank account objects
print("BANK ACCOUNT DEPOSIT OPERATIONS\n")

account1 = BankAccount("Alice Johnson", "ACC001", 5000)
account2 = BankAccount("Bob Smith", "ACC002", 3000)
account3 = BankAccount("Charlie Brown", "ACC003", 0)

# Display initial balance
account1.display_balance()
account2.display_balance()
account3.display_balance()

# Perform deposits
print("DEPOSITS")
print("=" * 60)

print(f"Account 1 Deposits:")
account1.deposit(1500)
account1.deposit(2000)
account1.deposit(500)

print(f"Account 2 Deposits:")
account2.deposit(1000)
account2.deposit(2500)

print(f"Account 3 Deposits:")
account3.deposit(10000)
account3.deposit(5000)

# Perform withdrawals
print("WITHDRAWALS")
print("=" * 60 + "\n")
account1.withdraw(2000)
account2.withdraw(1500)
account3.withdraw(3000)

# Apply interest
print("APPLYING INTEREST")
print("=" * 60 + "\n")
account1.apply_interest(5)
account2.apply_interest(4)
account3.apply_interest(5)

# Display final balances
print("FINAL ACCOUNT STATUS")
print("=" * 60)
account1.display_balance()
account2.display_balance()
account3.display_balance()

# Display transaction history
print("\nTRANSACTION HISTORY")
print("=" * 60)
account1.display_transaction_history()
account2.display_transaction_history()
account3.display_transaction_history()
