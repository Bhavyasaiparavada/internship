# Level 2: File Modes
import os

# 1. The w mode creates a file or replaces its old contents.
with open("mode_demo.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")

# 2. The a mode adds content to the end of the file.
with open("mode_demo.txt", "a") as file:
    file.write("Added with append mode\n")

# 3. The r mode reads the file.
with open("mode_demo.txt", "r") as file:
    print("3. Contents read with r mode:")
    print(file.read())

# 4. Difference between r, w, and a modes:
# r reads existing contents; w replaces contents; a adds to the end.
with open("mode_demo.txt", "a") as file:
    file.write("This line shows append mode\n")
with open("mode_demo.txt", "r") as file:
    print("4. Contents after appending:")
    print(file.read())

# 5. Check whether a file exists before opening it.
if os.path.exists("mode_demo.txt"):
    with open("mode_demo.txt", "r") as file:
        print("5. mode_demo.txt exists")
else:
    print("5. mode_demo.txt does not exist")

# 6. The x mode creates a new file only if it does not exist.
try:
    with open("new_file.txt", "x") as file:
        file.write("This file was just created.\n")
except FileExistsError:
    print("6. new_file.txt already exists")

# 7. Overwrite the file using w mode.
with open("overwrite.txt", "w") as file:
    file.write("Old contents\n")
with open("overwrite.txt", "w") as file:
    file.write("New contents replace the old contents\n")

# 8. Append student details to an existing file.
with open("student_details.txt", "w") as file:
    file.write("Asha, 19, Python\n")
with open("student_details.txt", "a") as file:
    file.write("Ben, 20, Python\n")

# 9. Clear all contents by opening the file in w mode and writing nothing.
with open("clear_me.txt", "w") as file:
    file.write("This text will be removed.\n")
with open("clear_me.txt", "w") as file:
    pass

# 10. Create a file, write data, read it, and append new data.
with open("complete_example.txt", "w") as file:
    file.write("First entry\n")
with open("complete_example.txt", "r") as file:
    print("10. Before appending:")
    print(file.read())
with open("complete_example.txt", "a") as file:
    file.write("Second entry\n")
with open("complete_example.txt", "r") as file:
    print("After appending:")
    print(file.read())
