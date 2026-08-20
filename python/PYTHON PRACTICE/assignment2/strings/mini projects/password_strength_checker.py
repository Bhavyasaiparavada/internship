password = input("Enter a password: ")

has_uppercase = False
has_lowercase = False
has_digit = False
has_special = False
for character in password:
    if character.isupper():
        has_uppercase = True
    elif character.islower():
        has_lowercase = True
    elif character.isdigit():
        has_digit = True
    else:
        has_special = True

strength_score = 0
if len(password) >= 8:
    strength_score += 1
if has_uppercase:
    strength_score += 1
if has_lowercase:
    strength_score += 1
if has_digit:
    strength_score += 1
if has_special:
    strength_score += 1

if strength_score <= 2:
    strength = "Weak"
elif strength_score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength:", strength)
