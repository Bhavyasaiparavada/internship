# Question 4: Create a BankAccount class with a class variable bank_name
# Create multiple accounts.

class BankAccount:
    bank_name = "Global Bank Ltd."
    
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def display_account_info(self):
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")
        print("-" * 40)
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder} deposited ${amount}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.account_holder} withdrew ${amount}")
        else:
            print(f"Insufficient balance for {self.account_holder}")


# Create multiple accounts
acc1 = BankAccount("ACC001", "Alice", 5000)
acc2 = BankAccount("ACC002", "Bob", 3000)
acc3 = BankAccount("ACC003", "Charlie", 7500)

# Display account information
print(f"Bank Name: {BankAccount.bank_name}\n")
acc1.display_account_info()
acc2.display_account_info()
acc3.display_account_info()

# Perform some operations
print("\n--- Transactions ---")
acc1.deposit(1000)
acc2.withdraw(500)
acc3.deposit(2000)

print("\n--- Updated Account Info ---")
acc1.display_account_info()
acc2.display_account_info()
acc3.display_account_info()
