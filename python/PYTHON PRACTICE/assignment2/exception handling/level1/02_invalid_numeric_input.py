try:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    print("Sum:", first + second)
except ValueError:
    print("Please enter valid numbers.")