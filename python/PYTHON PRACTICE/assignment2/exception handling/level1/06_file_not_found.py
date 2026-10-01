try:
    file = open("notes.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("The file notes.txt was not found.")