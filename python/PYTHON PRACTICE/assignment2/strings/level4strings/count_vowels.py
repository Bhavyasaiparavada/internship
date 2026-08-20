text = input("Enter a string: ")

vowel_count = 0
for character in text:
    if character.lower() in "aeiou":
        vowel_count += 1

print("Number of vowels:", vowel_count)
