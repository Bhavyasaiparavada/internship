try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Division by Zero is Not Allowed")