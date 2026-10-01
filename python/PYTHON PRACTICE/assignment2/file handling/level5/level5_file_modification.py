# Level 5: File Modification

# Sample number file for exercises 1 and 2.
with open("numbers.txt", "w") as file:
    for number in range(1, 11):
        file.write(str(number) + "\n")

# 1. Write only even numbers to another file.
with open("numbers.txt", "r") as file:
    numbers = [int(line) for line in file]
with open("even_numbers.txt", "w") as file:
    for number in numbers:
        if number % 2 == 0:
            file.write(str(number) + "\n")

# 2. Write only odd numbers to another file.
with open("odd_numbers.txt", "w") as file:
    for number in numbers:
        if number % 2 != 0:
            file.write(str(number) + "\n")

# Input for the text exercises below.
example_text = """Python is fun.

File handling is fun.
Python is simple.
File handling is fun.
"""
with open("text_to_change.txt", "w") as file:
    file.write(example_text)

with open("text_to_change.txt", "r") as file:
    lines = file.readlines()

# 3. Replace one word with another word.
with open("replaced_text.txt", "w") as file:
    for line in lines:
        file.write(line.replace("fun", "useful"))

# 4. Remove blank lines.
with open("without_blank_lines.txt", "w") as file:
    for line in lines:
        if line.strip() != "":
            file.write(line)

# 5. Remove extra spaces from each line.
with open("text_with_extra_spaces.txt", "w") as file:
    file.write("Python    is   easy.\nFile   handling   is useful.\n")
with open("text_with_extra_spaces.txt", "r") as file:
    clean_lines = [" ".join(line.split()) for line in file]
with open("without_extra_spaces.txt", "w") as file:
    for line in clean_lines:
        file.write(line + "\n")

# 6. Convert all text to uppercase in a new file.
with open("uppercase_text.txt", "w") as file:
    for line in lines:
        file.write(line.upper())

# 7. Convert all text to lowercase in a new file.
with open("lowercase_text.txt", "w") as file:
    for line in lines:
        file.write(line.lower())

# 8. Reverse each line and write the result to another file.
with open("reversed_lines.txt", "w") as file:
    for line in lines:
        if line.endswith("\n"):
            file.write(line[:-1][::-1] + "\n")
        else:
            file.write(line[::-1])

# 9. Write the lines in reverse order to another file.
with open("reverse_order.txt", "w") as file:
    for line in lines[::-1]:
        file.write(line)

# 10. Remove duplicate lines, keeping the first occurrence.
unique_lines = []
for line in lines:
    if line not in unique_lines:
        unique_lines.append(line)
with open("without_duplicate_lines.txt", "w") as file:
    file.writelines(unique_lines)
