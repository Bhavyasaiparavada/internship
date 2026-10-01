class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        self.balance += self.balance * rate / 100


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount


savings = SavingsAccount("Asha", 1000)
savings.add_interest(5)
print("Savings balance:", savings.balance)
current = CurrentAccount("Ravi", 1000)
current.withdraw(100)
print("Current balance:", current.balance)
