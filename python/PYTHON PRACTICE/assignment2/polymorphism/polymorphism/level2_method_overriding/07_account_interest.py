class BankAccount:
    def calculate_interest(self, balance):
        return balance * 0.02


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.05


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.01


savings_account = SavingsAccount()
current_account = CurrentAccount()
print("Savings account interest:", savings_account.calculate_interest(10000))
print("Current account interest:", current_account.calculate_interest(10000))