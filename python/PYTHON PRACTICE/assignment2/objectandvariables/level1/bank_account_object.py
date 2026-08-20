class BankAccount:
    def __init__(self, account_holder_name, account_number):
        self.account_holder_name = account_holder_name
        self.account_number = account_number


account = BankAccount("Sneha Sharma", "SB123456789")
print("Account holder:", account.account_holder_name)
print("Account number:", account.account_number)
