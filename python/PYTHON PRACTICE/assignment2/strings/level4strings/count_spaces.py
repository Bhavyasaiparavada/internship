text = input("Enter a string: ")

space_count = 0
for character in text:
    if character == " ":
        space_count += 1

print("Number of spaces:", space_count)
