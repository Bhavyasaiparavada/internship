sentence = input("Enter a sentence: ")

words = sentence.split()
reversed_order = ""
for word in words:
    reversed_order = word + " " + reversed_order

print("Words in reverse order:", reversed_order.strip())
