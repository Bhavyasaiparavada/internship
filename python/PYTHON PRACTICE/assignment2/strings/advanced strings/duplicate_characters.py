text = input("Enter a string: ")

frequencies = {}
for character in text:
    frequencies[character] = frequencies.get(character, 0) + 1

duplicates = ""
for character in text:
    if frequencies[character] > 1 and character not in duplicates:
        duplicates += character

if duplicates:
    print("Duplicate characters:", duplicates)
else:
    print("There are no duplicate characters.")
