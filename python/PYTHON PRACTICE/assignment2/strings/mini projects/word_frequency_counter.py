paragraph = input("Enter a paragraph: ")

frequencies = {}
current_word = ""
for character in paragraph.lower():
    if character.isalnum():
        current_word += character
    elif current_word:
        frequencies[current_word] = frequencies.get(current_word, 0) + 1
        current_word = ""

if current_word:
    frequencies[current_word] = frequencies.get(current_word, 0) + 1

for word, frequency in frequencies.items():
    print(word, ":", frequency)
