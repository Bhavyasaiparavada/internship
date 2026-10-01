try:
    with open("numbers.txt", "r") as file:
        numbers = [float(line) for line in file]
    print("Numbers:", numbers)
except FileNotFoundError:
    print("The file numbers.txt was not found.")
except PermissionError:
    print("You do not have permission to read the file.")
except ValueError:
    print("The file contains a line that is not a number.")