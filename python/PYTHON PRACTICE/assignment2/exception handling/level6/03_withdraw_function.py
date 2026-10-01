def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount


try:
    print("New balance:", withdraw(500, float(input("Withdrawal amount: "))))
except ValueError as error:
    print("Withdrawal failed:", error)