text = input("Enter a string: ")

frequencies = {}
for character in text:
    frequencies[character] = frequencies.get(character, 0) + 1

first_non_repeated = None
for character in text:
    if frequencies[character] == 1:
        first_non_repeated = character
        break

if first_non_repeated is None:
    print("There is no non-repeated character.")
else:
    print("First non-repeated character:", first_non_repeated)
