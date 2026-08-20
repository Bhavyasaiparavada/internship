sentence = input("Enter a sentence: ")

capitalized_sentence = ""
start_of_word = True
for character in sentence:
    if character.isspace():
        capitalized_sentence += character
        start_of_word = True
    elif start_of_word:
        capitalized_sentence += character.upper()
        start_of_word = False
    else:
        capitalized_sentence += character

print("Capitalized sentence:", capitalized_sentence)
