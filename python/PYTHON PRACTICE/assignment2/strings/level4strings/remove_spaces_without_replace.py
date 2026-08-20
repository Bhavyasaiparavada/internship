text = input("Enter a string: ")

text_without_spaces = ""
for character in text:
    if character != " ":
        text_without_spaces += character

print("String without spaces:", text_without_spaces)
