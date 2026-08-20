class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance


accounts = [
    BankAccount("Neha Kapoor", "BA1001", 45000),
    BankAccount("Rahul Iyer", "BA1002", 68500),
]

for account in accounts:
    print("Account holder:", account.account_holder)
    print("Account number:", account.account_number)
    print("Balance: Rs.", account.balance)
    print()
