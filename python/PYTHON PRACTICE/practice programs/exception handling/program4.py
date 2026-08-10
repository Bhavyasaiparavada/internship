try:
    filename = input("Enter File Name: ")

    file = open(filename, "r")
    print(file.read())

    file.close()

except FileNotFoundError:
    print("File Not Found")