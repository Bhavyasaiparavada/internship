# Level 4: File Processing

sample_text = """Python File Practice
Python is EASY.
I like python programs.

File handling is useful in Python.
"""
with open("processing_sample.txt", "w") as file:
    file.write(sample_text)

with open("processing_sample.txt", "r") as file:
    contents = file.read()

# 1. Count the total number of lines.
print("1. Total lines:", len(contents.splitlines()))

# 2. Count the total number of words.
print("2. Total words:", len(contents.split()))

# 3. Count the total number of characters, including spaces and newlines.
print("3. Total characters:", len(contents))

# 4. Count vowels.
vowels = "aeiouAEIOU"
print("4. Vowels:", sum(1 for character in contents if character in vowels))

# 5. Count consonants (alphabetic letters that are not vowels).
consonants = sum(
    1 for character in contents
    if character.isalpha() and character not in vowels
)
print("5. Consonants:", consonants)

# 6. Count digits.
print("6. Digits:", sum(1 for character in contents if character.isdigit()))

# 7. Count space characters.
print("7. Spaces:", contents.count(" "))

# 8. Count uppercase and lowercase characters.
uppercase_count = sum(1 for character in contents if character.isupper())
lowercase_count = sum(1 for character in contents if character.islower())
print("8. Uppercase:", uppercase_count)
print("   Lowercase:", lowercase_count)

# 9. Display lines containing a particular word (case-insensitive).
print("9. Lines containing 'python':")
with open("processing_sample.txt", "r") as file:
    for line in file:
        if "python" in line.lower():
            print(line, end="")

# 10. Display lines that start with a particular character.
start_character = "P"
print("10. Lines starting with", repr(start_character) + ":")
with open("processing_sample.txt", "r") as file:
    for line in file:
        if line.startswith(start_character):
            print(line, end="")
