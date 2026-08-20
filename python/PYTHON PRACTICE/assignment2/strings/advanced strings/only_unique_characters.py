text = input("Enter a string: ")

frequencies = {}
for character in text:
    frequencies[character] = frequencies.get(character, 0) + 1

only_unique = True
for frequency in frequencies.values():
    if frequency > 1:
        only_unique = False
        break

if only_unique:
    print("The string contains only unique characters.")
else:
    print("The string does not contain only unique characters.")
