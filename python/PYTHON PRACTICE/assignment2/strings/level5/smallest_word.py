sentence = input("Enter a sentence: ")

words = sentence.split()
smallest = None
for word in words:
    if smallest is None or len(word) < len(smallest):
        smallest = word

if smallest is None:
    print("The sentence has no words.")
else:
    print("Smallest word:", smallest)
