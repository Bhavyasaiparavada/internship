class BankAccount:
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number


account = BankAccount("Ravi", "123456")
print(account.account_holder, account.account_number)