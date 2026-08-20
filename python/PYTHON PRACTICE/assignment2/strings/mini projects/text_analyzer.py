text = input("Enter text: ")

character_count = len(text)
word_count = 0
vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = 0
special_character_count = 0
inside_word = False

for character in text:
    if character.isspace():
        space_count += 1
        inside_word = False
    else:
        if not inside_word:
            word_count += 1
            inside_word = True
        if character.isdigit():
            digit_count += 1
        elif character.isalpha():
            if character.lower() in "aeiou":
                vowel_count += 1
            else:
                consonant_count += 1
        else:
            special_character_count += 1

print("Characters:", character_count)
print("Words:", word_count)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Digits:", digit_count)
print("Spaces:", space_count)
print("Special characters:", special_character_count)
