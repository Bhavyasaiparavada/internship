text = input("Enter a string: ")

seen_characters = set()
first_repeated = None
for character in text:
    if character in seen_characters:
        first_repeated = character
        break
    seen_characters.add(character)

if first_repeated is None:
    print("There is no repeated character.")
else:
    print("First repeated character:", first_repeated)
