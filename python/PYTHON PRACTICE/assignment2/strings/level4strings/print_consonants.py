text = input("Enter a string: ")

for character in text:
    if character.isalpha() and character.lower() not in "aeiou":
        print(character)
