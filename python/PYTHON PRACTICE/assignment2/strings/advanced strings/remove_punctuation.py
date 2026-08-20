text = input("Enter a string: ")

without_punctuation = ""
for character in text:
    if character.isalnum() or character.isspace():
        without_punctuation += character

print("String without punctuation:", without_punctuation)
