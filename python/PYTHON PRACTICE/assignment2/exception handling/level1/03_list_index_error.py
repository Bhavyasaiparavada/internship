items = ["apple", "banana", "orange"]

try:
    index = int(input("Enter a list index: "))
    print(items[index])
except IndexError:
    print("That index is outside the list.")
except ValueError:
    print("Please enter a whole number.")