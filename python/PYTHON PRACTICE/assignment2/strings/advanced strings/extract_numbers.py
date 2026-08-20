text = input("Enter a string: ")

numbers = []
current_number = ""
for character in text:
    if character.isdigit():
        current_number += character
    elif current_number:
        numbers.append(current_number)
        current_number = ""

if current_number:
    numbers.append(current_number)

if numbers:
    print("Numbers:", " ".join(numbers))
else:
    print("No numbers found.")
