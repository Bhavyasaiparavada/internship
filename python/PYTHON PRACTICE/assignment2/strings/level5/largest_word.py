sentence = input("Enter a sentence: ")

words = sentence.split()
largest = ""
for word in words:
    if len(word) > len(largest):
        largest = word

if largest:
    print("Largest word:", largest)
else:
    print("The sentence has no words.")
