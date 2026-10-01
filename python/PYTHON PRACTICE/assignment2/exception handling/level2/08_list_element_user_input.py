items = ["red", "green", "blue"]

try:
    index = int(input("Enter a list index: "))
    print(items[index])
except ValueError:
    print("Please enter a whole-number index.")
except IndexError:
    print("That index is outside the list.")