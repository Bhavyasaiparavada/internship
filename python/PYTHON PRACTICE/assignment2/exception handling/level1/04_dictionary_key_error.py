ages = {"Asha": 20, "Ravi": 22}

try:
    name = input("Enter a name: ")
    print(ages[name])
except KeyError:
    print("That name is not in the dictionary.")