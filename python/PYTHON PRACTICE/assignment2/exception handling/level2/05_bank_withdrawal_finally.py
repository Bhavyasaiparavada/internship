balance = 500

try:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    if amount > balance:
        raise ValueError("Not enough money in the account.")
    balance -= amount
    print("Withdrawal complete. Balance:", balance)
except ValueError as error:
    print("Withdrawal failed:", error)
finally:
    print("Thank you for using the bank.")