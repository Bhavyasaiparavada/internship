sentence = input("Enter a sentence: ")

reversed_sentence = ""
current_word = ""
for character in sentence:
    if character.isspace():
        for word_character in current_word:
            reversed_sentence = word_character + reversed_sentence
        reversed_sentence = character + reversed_sentence
        current_word = ""
    else:
        current_word += character

for word_character in current_word:
    reversed_sentence = word_character + reversed_sentence

print("Each word reversed:", reversed_sentence)
