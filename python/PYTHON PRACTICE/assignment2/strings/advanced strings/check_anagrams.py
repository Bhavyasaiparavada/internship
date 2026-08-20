first_text = input("Enter the first string: ")
second_text = input("Enter the second string: ")

first_cleaned = ""
second_cleaned = ""
for character in first_text:
    if not character.isspace():
        first_cleaned += character.lower()
for character in second_text:
    if not character.isspace():
        second_cleaned += character.lower()

if sorted(first_cleaned) == sorted(second_cleaned):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
