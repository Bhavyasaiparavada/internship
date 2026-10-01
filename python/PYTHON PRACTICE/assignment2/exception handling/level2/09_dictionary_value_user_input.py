prices = {"pen": 2, "book": 10, "bag": 25}

key = input("Enter an item name: ")
try:
    print("Price:", prices[key])
except KeyError:
    print("That item is not in the dictionary.")