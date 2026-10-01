from abc import ABC, abstractmethod


class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return 500


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return 0


print("Savings interest:", SavingsAccount().calculate_interest())
print("Current interest:", CurrentAccount().calculate_interest())