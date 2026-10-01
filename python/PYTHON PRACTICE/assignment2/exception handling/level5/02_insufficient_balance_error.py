class InsufficientBalanceError(Exception):
    pass


balance = 500
try:
    amount = float(input("Enter withdrawal amount: "))
    if amount > balance:
        raise InsufficientBalanceError("Not enough money in the account.")
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    print("Remaining balance:", balance - amount)
except ValueError as error:
    print("Invalid amount:", error)
except InsufficientBalanceError as error:
    print(error)