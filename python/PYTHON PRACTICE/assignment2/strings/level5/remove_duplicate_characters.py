text = input("Enter a string: ")

unique_text = ""
for character in text:
    if character not in unique_text:
        unique_text += character

print("String without duplicate characters:", unique_text)
