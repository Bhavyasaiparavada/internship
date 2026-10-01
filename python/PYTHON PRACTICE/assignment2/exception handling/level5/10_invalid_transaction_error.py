class InvalidTransactionError(Exception):
    pass


try:
    transaction_type = input("Enter deposit or withdrawal: ").lower()
    amount = float(input("Enter amount: "))
    if transaction_type not in ("deposit", "withdrawal") or amount <= 0:
        raise InvalidTransactionError("Choose deposit or withdrawal and enter a positive amount.")
    print("Transaction accepted.")
except ValueError:
    print("Enter the amount as a number.")
except InvalidTransactionError as error:
    print(error)