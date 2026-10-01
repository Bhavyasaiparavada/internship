class StringOperations:
    def reverse(self, text):
        return text[::-1]

    def count_vowels(self, text):
        count = 0
        for character in text.lower():
            if character in "aeiou":
                count += 1
        return count

    def is_palindrome(self, text):
        return text.lower() == text.lower()[::-1]


operations = StringOperations()
print(operations.reverse("python"))
print("Vowels:", operations.count_vowels("python"))
print("Palindrome:", operations.is_palindrome("level"))