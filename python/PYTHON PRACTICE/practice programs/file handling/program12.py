file = open("student.txt", "r")

lines = file.readlines()
file.close()

line_number = int(input("Enter line number to update: "))
new_line = input("Enter new text: ")

lines[line_number - 1] = new_line + "\n"

file = open("student.txt", "w")

file.writelines(lines)

file.close()