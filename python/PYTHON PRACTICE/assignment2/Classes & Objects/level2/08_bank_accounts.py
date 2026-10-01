class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance


accounts = [BankAccount("Asha", "1001", 5000), BankAccount("Ravi", "1002", 8000)]
for account in accounts:
    print(account.account_holder, account.account_number, account.balance)