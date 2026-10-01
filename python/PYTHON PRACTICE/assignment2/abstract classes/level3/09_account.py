from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def account_type(self):
        pass


class SavingsAccount(Account):
    def account_type(self):
        return "Savings account"


class CurrentAccount(Account):
    def account_type(self):
        return "Current account"


for account in [SavingsAccount("S100", 1500), CurrentAccount("C200", 3000)]:
    print(account.account_type(), account.account_number, account.balance)