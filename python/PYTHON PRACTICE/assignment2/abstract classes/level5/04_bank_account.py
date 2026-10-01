from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass

    def display_balance(self):
        return "Balance: " + str(self.balance)


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.05


account = SavingsAccount(10000)
print(account.display_balance())
print("Interest:", account.calculate_interest())