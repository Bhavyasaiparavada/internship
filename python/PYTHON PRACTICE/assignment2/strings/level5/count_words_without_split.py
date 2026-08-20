sentence = input("Enter a sentence: ")

word_count = 0
inside_word = False
for character in sentence:
    if character.isspace():
        inside_word = False
    elif not inside_word:
        word_count += 1
        inside_word = True

print("Number of words:", word_count)
