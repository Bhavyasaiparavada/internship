try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("That was not a whole number.")
finally:
    print("The finally block always runs.")