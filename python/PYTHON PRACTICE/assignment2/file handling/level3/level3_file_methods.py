# Level 3: File Methods

with open("method_sample.txt", "w") as file:
    file.write("Python makes file handling simple.\n")
    file.write("This is the second line.\n")

# 1. read() reads the complete contents.
with open("method_sample.txt", "r") as file:
    print("1. Complete contents:")
    print(file.read())

# 2. read(n) reads only the first n characters.
with open("method_sample.txt", "r") as file:
    print("2. First 6 characters:", file.read(6))

# 3. readline() reads one line at a time.
with open("method_sample.txt", "r") as file:
    print("3. First line:", file.readline(), end="")
    print("Second line:", file.readline(), end="")

# 4. readlines() returns all lines in a list.
with open("method_sample.txt", "r") as file:
    lines = file.readlines()
print("4. Lines:", lines)

# 5. write() writes a single line.
with open("write_example.txt", "w") as file:
    file.write("A single line written with write().\n")

# 6. writelines() writes a list of strings. Include newline characters yourself.
with open("writelines_example.txt", "w") as file:
    file.writelines(["First line\n", "Second line\n", "Third line\n"])

# 7. tell() displays the current file pointer position.
with open("method_sample.txt", "r") as file:
    print("7. Position at the start:", file.tell())
    file.read(6)
    print("Position after reading 6 characters:", file.tell())

# 8. seek() moves the file pointer to a specific position.
with open("method_sample.txt", "r") as file:
    file.seek(7)
    print("8. Text from position 7:", file.read())

# 9. Use seek() and tell() together to show pointer movement.
with open("method_sample.txt", "r") as file:
    print("9. Starting position:", file.tell())
    file.seek(7)
    print("Position after seek(7):", file.tell())
    file.read(5)
    print("Position after reading 5 characters:", file.tell())

# 10. with open() closes the file safely when the block ends.
with open("method_sample.txt", "r") as file:
    safe_contents = file.read()
print("10. Read safely with with open():")
print(safe_contents)
