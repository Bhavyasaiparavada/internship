text = input("Enter a string: ")

frequencies = {}
for character in text:
    if character in frequencies:
        frequencies[character] += 1
    else:
        frequencies[character] = 1

for character, frequency in frequencies.items():
    print(repr(character), ":", frequency)
