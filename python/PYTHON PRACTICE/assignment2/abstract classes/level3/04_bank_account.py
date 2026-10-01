from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return 500


account = SavingsAccount("Asha", "12345")
print(account.account_holder, account.account_number)
print("Interest:", account.calculate_interest())