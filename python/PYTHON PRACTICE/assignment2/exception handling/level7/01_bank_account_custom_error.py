class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough money in the account.")
        self.balance -= amount
        return self.balance


account = BankAccount(500)
try:
    print("Balance:", account.withdraw(100))
except InsufficientBalanceError as error:
    print(error)