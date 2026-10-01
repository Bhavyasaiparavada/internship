items = ["tea", "coffee", "water"]

try:
    index = int(input("Enter a list index: "))
    print(items[index])
except ValueError:
    print("Enter the index as a whole number.")
except IndexError:
    print("That index is outside the list.")