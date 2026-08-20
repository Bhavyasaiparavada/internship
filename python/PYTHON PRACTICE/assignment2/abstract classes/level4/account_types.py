from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.04


class CurrentAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.01


accounts = [SavingsAccount("SA1001", 20000), CurrentAccount("CA2002", 20000)]
for account in accounts:
    print(account.account_number, "Interest: Rs.", account.calculate_interest())
