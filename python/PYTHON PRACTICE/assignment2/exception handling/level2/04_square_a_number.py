try:
    number = float(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number.")
else:
    print("Square:", number * number)