while True:
    print("\nString Menu")
    print("1. Reverse string")
    print("2. Check palindrome")
    print("3. Count vowels")
    print("4. Count words")
    print("5. Character frequency")
    print("6. Convert to uppercase")
    print("7. Convert to lowercase")
    print("8. Exit")

    choice = input("Enter your choice: ")
    if choice == "8":
        print("Exiting program.")
        break
    if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
        print("Invalid choice.")
        continue

    text = input("Enter a string: ")
    if choice == "1":
        reversed_text = ""
        for character in text:
            reversed_text = character + reversed_text
        print("Reversed string:", reversed_text)
    elif choice == "2":
        reversed_text = ""
        for character in text:
            reversed_text = character + reversed_text
        print("The string is a palindrome." if text == reversed_text else "The string is not a palindrome.")
    elif choice == "3":
        vowel_count = 0
        for character in text.lower():
            if character in "aeiou":
                vowel_count += 1
        print("Number of vowels:", vowel_count)
    elif choice == "4":
        word_count = 0
        inside_word = False
        for character in text:
            if character.isspace():
                inside_word = False
            elif not inside_word:
                word_count += 1
                inside_word = True
        print("Number of words:", word_count)
    elif choice == "5":
        frequencies = {}
        for character in text:
            frequencies[character] = frequencies.get(character, 0) + 1
        for character, frequency in frequencies.items():
            print(repr(character), ":", frequency)
    elif choice == "6":
        print("Uppercase string:", text.upper())
    elif choice == "7":
        print("Lowercase string:", text.lower())
