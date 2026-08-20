text = input("Enter a string: ")

for character in text:
    if character.lower() in "aeiou":
        print(character)
