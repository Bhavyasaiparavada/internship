file = open("student.txt", "r")

data = file.read()

word = input("Enter word to search: ")

if word in data:
    print("Word Found")
else:
    print("Word Not Found")

file.close()