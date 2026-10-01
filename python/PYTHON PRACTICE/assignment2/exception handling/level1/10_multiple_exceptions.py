try:
    numbers = [10, 20, 30]
    index = int(input("Enter an index: "))
    divisor = int(input("Enter a divisor: "))
    print(numbers[index] / divisor)
except ValueError:
    print("Please enter whole numbers.")
except IndexError:
    print("That index is outside the list.")
except ZeroDivisionError:
    print("A number cannot be divided by zero.")