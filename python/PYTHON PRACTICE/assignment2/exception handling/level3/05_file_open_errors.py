file_name = input("Enter a file name: ")

try:
    with open(file_name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to open that file.")