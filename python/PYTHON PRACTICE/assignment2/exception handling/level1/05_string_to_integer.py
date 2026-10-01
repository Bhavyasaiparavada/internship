try:
    number = int(input("Enter a whole number: "))
    print("Number:", number)
except ValueError:
    print("That string is not a valid whole number.")