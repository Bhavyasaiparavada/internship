# Level 1: Basic File Operations

# 1. Create a text file and write a message.
with open("sample.txt", "w") as file:
    file.write("Welcome to Python")

# 2. Write personal details (replace these example values with your own).
with open("personal_details.txt", "w") as file:
    file.write("Name: Your Name\n")
    file.write("Age: Your Age\n")
    file.write("Course: Your Course\n")

# 3. Write five student names.
student_names = ["Asha", "Ben", "Chitra", "David", "Elena"]
with open("students.txt", "w") as file:
    for name in student_names:
        file.write(name + "\n")

# 4. Write five numbers, one per line.
with open("numbers.txt", "w") as file:
    for number in [10, 20, 30, 40, 50]:
        file.write(str(number) + "\n")

# 5. Read and display the complete contents of a file.
with open("sample.txt", "r") as file:
    print("5. Complete contents:")
    print(file.read())

# 6. Read and display a file character by character.
print("6. Characters:")
with open("sample.txt", "r") as file:
    for character in file.read():
        print(character)

# 7. Read and display a file line by line.
print("7. Student names, one per line:")
with open("students.txt", "r") as file:
    for line in file:
        print(line, end="")

# 8. Read all lines into a list.
with open("students.txt", "r") as file:
    student_lines = file.readlines()
print("8. Lines stored in a list:", student_lines)

# 9. Display the first five lines.
print("9. First five lines:")
with open("students.txt", "r") as file:
    for line_number in range(5):
        line = file.readline()
        if line == "":
            break
        print(line, end="")

# 10. Display the last five lines.
with open("students.txt", "r") as file:
    all_lines = file.readlines()
print("10. Last five lines:")
for line in all_lines[-5:]:
    print(line, end="")
