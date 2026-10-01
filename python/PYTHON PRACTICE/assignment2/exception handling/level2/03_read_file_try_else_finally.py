file = None

try:
    file = open("notes.txt", "r")
except FileNotFoundError:
    print("The file notes.txt was not found.")
else:
    print(file.read())
finally:
    if file is not None:
        file.close()
    print("File handling is finished.")