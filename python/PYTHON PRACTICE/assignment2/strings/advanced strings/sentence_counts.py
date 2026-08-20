sentence = input("Enter a sentence: ")

word_count = 0
character_count = 0
digit_count = 0
vowel_count = 0
space_count = 0
inside_word = False
for character in sentence:
    character_count += 1
    if character.isspace():
        space_count += 1
        inside_word = False
    else:
        if not inside_word:
            word_count += 1
            inside_word = True
        if character.isdigit():
            digit_count += 1
        if character.lower() in "aeiou":
            vowel_count += 1

print("Number of words:", word_count)
print("Number of characters:", character_count)
print("Number of digits:", digit_count)
print("Number of vowels:", vowel_count)
print("Number of spaces:", space_count)
