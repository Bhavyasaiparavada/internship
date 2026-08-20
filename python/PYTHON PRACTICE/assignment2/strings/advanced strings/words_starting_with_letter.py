sentence = input("Enter a sentence: ")
letter = input("Enter the starting letter: ")

matching_words = []
for word in sentence.split():
    if word and word[0].lower() == letter.lower():
        matching_words.append(word)

if matching_words:
    print("Matching words:", " ".join(matching_words))
else:
    print("No words found.")
