try:
    balance = 5000
    amount = int(input("Enter Withdrawal Amount: "))

    if amount <= 0:
        raise Exception("Invalid Amount")

    if amount > balance:
        raise Exception("Insufficient Balance")

    balance = balance - amount
    print("Remaining Balance:", balance)

except Exception as e:
    print(e)