from abc import ABC, abstractmethod


class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self, balance):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.04


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.01


print("Savings account interest:", SavingsAccount().calculate_interest(10000))
print("Current account interest:", CurrentAccount().calculate_interest(10000))
