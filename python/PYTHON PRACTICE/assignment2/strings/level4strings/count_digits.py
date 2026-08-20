text = input("Enter a string: ")

digit_count = 0
for character in text:
    if character.isdigit():
        digit_count += 1

print("Number of digits:", digit_count)
