from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self, balance):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.04


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.01


accounts = [
    SavingsAccount("Priya", "SA1001"),
    CurrentAccount("Arun", "CA2002"),
]
for account in accounts:
    interest = account.calculate_interest(10000)
    print(account.account_holder, account.account_number, "Interest: Rs.", interest)
