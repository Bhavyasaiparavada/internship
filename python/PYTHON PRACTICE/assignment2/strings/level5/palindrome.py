text = input("Enter a string: ")

reversed_text = ""
for character in text:
    reversed_text = character + reversed_text

if text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
