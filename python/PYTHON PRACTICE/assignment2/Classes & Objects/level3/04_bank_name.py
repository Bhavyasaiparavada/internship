class BankAccount:
    bank_name = "National Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder


accounts = [BankAccount("Asha"), BankAccount("Ravi")]
for account in accounts:
    print(account.account_holder, account.bank_name)