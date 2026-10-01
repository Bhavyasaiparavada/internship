try:
    with open("notes.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Cannot read the file because it does not exist.")