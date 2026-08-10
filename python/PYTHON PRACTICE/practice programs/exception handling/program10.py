try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = num1 / num2

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Division by Zero is Not Allowed")

else:
    print("Result:", result)

finally:
    print("Program Completed")