items = ["Monday", "Tuesday", "Wednesday"]

try:
    index = int(input("Enter an index: "))
    print(items[index])
except ValueError:
    print("The index must be a whole number.")
except IndexError:
    print("The index is outside the list.")
except TypeError:
    print("The index has an unsupported type.")