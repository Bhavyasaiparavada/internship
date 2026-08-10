file = open("student.txt", "r")

lines = file.readlines()
file.close()

line_number = int(input("Enter line number to delete: "))

file = open("student.txt", "w")

for i in range(len(lines)):
    if i != line_number - 1:
        file.write(lines[i])

file.close()