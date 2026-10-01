data = {"one": 1, "two": 2}

try:
    key = input("Enter a key (one or two): ")
    print(data[key])
except KeyError:
    print("That key is not in the dictionary.")
except TypeError:
    print("The key has an unsupported type.")