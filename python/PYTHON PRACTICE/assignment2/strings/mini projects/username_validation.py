username = input("Enter a username: ")

is_valid = True
if len(username) < 3 or len(username) > 15:
    is_valid = False
elif not username[0].isalpha():
    is_valid = False
else:
    for character in username:
        if not (character.isalnum() or character == "_"):
            is_valid = False
            break

if is_valid:
    print("Username is valid.")
else:
    print("Username is invalid. Use 3-15 characters, start with a letter, and use only letters, digits, or underscores.")
