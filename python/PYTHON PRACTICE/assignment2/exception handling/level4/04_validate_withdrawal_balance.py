balance = 1000

try:
    amount = float(input("Enter withdrawal amount: "))
    if amount > balance:
        raise ValueError("Withdrawal is greater than the available balance.")
    if amount <= 0:
        raise ValueError("Withdrawal must be positive.")
    print("Remaining balance:", balance - amount)
except ValueError as error:
    print("Withdrawal error:", error)