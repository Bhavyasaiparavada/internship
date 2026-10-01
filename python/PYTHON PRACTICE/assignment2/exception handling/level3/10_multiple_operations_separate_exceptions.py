try:
    values = [10, 20, 30]
    index = int(input("Enter a list index: "))
    divisor = int(input("Enter a divisor: "))
    print("Result:", values[index] / divisor)
except ValueError:
    print("Please enter whole numbers.")
except IndexError:
    print("That index is outside the list.")
except ZeroDivisionError:
    print("A number cannot be divided by zero.")
except TypeError:
    print("The operation used an unsupported type.")