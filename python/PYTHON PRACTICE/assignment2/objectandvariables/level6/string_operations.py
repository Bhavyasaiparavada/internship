# Question 8: Create a StringOperations class with methods to reverse a string, count vowels, and check palindrome.

class StringOperations:
    def __init__(self, text=""):
        """Initialize string operations"""
        self.text = text
    
    def reverse_string(self, string=None):
        """
        Reverse a string
        Method accepts string parameter and returns reversed string
        """
        s = string if string is not None else self.text
        return s[::-1]
    
    def count_vowels(self, string=None):
        """Count vowels in a string"""
        s = string if string is not None else self.text
        vowels = "aeiouAEIOU"
        count = sum(1 for char in s if char in vowels)
        return count
    
    def count_consonants(self, string=None):
        """Count consonants in a string"""
        s = string if string is not None else self.text
        consonants = 0
        for char in s:
            if char.isalpha() and char.lower() not in "aeiou":
                consonants += 1
        return consonants
    
    def is_palindrome(self, string=None):
        """
        Check if a string is palindrome
        Method accepts string parameter and returns boolean
        """
        s = string if string is not None else self.text
        # Remove spaces and convert to lowercase
        cleaned = s.replace(" ", "").lower()
        return cleaned == cleaned[::-1]
    
    def count_words(self, string=None):
        """Count number of words"""
        s = string if string is not None else self.text
        return len(s.split())
    
    def count_characters(self, string=None, include_spaces=True):
        """Count total characters"""
        s = string if string is not None else self.text
        if include_spaces:
            return len(s)
        else:
            return len(s.replace(" ", ""))
    
    def uppercase_string(self, string=None):
        """Convert string to uppercase"""
        s = string if string is not None else self.text
        return s.upper()
    
    def lowercase_string(self, string=None):
        """Convert string to lowercase"""
        s = string if string is not None else self.text
        return s.lower()
    
    def count_specific_char(self, char, string=None):
        """Count occurrences of specific character"""
        s = string if string is not None else self.text
        return s.count(char)
    
    def display_string_analysis(self, string=None):
        """Display complete string analysis"""
        s = string if string is not None else self.text
        
        print(f"\n{'='*60}")
        print(f"STRING ANALYSIS")
        print(f"{'='*60}")
        print(f"Original String: {s}")
        print(f"Reversed String: {self.reverse_string(s)}")
        print(f"{'='*60}")
        print(f"Total Characters: {self.count_characters(s, include_spaces=True)}")
        print(f"Characters (no spaces): {self.count_characters(s, include_spaces=False)}")
        print(f"Words: {self.count_words(s)}")
        print(f"Vowels: {self.count_vowels(s)}")
        print(f"Consonants: {self.count_consonants(s)}")
        print(f"Is Palindrome: {'Yes' if self.is_palindrome(s) else 'No'}")
        print(f"Uppercase: {self.uppercase_string(s)}")
        print(f"Lowercase: {self.lowercase_string(s)}")
        print(f"{'='*60}\n")


# Create string operations object
print("STRING OPERATIONS\n")

str_ops = StringOperations()

# Test reverse string
print("REVERSE STRING")
print("=" * 60)
test_strings = ["Hello", "Python", "World"]
for string in test_strings:
    reversed_str = str_ops.reverse_string(string)
    print(f"Original: {string:20} | Reversed: {reversed_str}")

print()

# Test vowel count
print("\nVOWEL COUNT")
print("=" * 60)
test_strings = ["Hello World", "Python Programming", "Aeiou"]
for string in test_strings:
    vowel_count = str_ops.count_vowels(string)
    consonant_count = str_ops.count_consonants(string)
    print(f"{string:25} | Vowels: {vowel_count} | Consonants: {consonant_count}")

print()

# Test palindrome check
print("\nPALINDROME CHECK")
print("=" * 60)
test_strings = ["racecar", "hello", "madam", "Python", "A man a plan a canal Panama"]
for string in test_strings:
    is_pal = "Palindrome" if str_ops.is_palindrome(string) else "Not Palindrome"
    print(f"{string:35} | {is_pal}")

print()

# Character and word count
print("\n\nCHARACTER AND WORD COUNT")
print("=" * 60)
test_strings = ["Hello World", "Python is great", "The quick brown fox"]
for string in test_strings:
    chars = str_ops.count_characters(string)
    words = str_ops.count_words(string)
    print(f"{string:25} | Characters: {chars:2} | Words: {words}")

print()

# Detailed string analysis
print("\n\nDETAILED STRING ANALYSIS")
print("=" * 60)
test_strings = ["Hello", "Radar", "Programming"]
for string in test_strings:
    str_ops.display_string_analysis(string)

# Count specific character
print("\nSPECIFIC CHARACTER COUNT")
print("=" * 60)
string = "Mississippi"
for char in set(string.lower()):
    count = str_ops.count_specific_char(char, string)
    print(f"Character '{char}' appears {count} time(s) in '{string}'")

print()

# String transformations
print("\n\nSTRING TRANSFORMATIONS")
print("=" * 60)
original = "Hello World"
print(f"Original: {original}")
print(f"Uppercase: {str_ops.uppercase_string(original)}")
print(f"Lowercase: {str_ops.lowercase_string(original)}")
print(f"Reversed: {str_ops.reverse_string(original)}")

# Complex palindrome examples
print("\n\nCOMPLEX PALINDROME EXAMPLES")
print("=" * 60)
complex_strings = [
    "A man a plan a canal Panama",
    "Was it a car or a cat I saw",
    "Do geese see God",
    "Hello there"
]
for string in complex_strings:
    is_pal = str_ops.is_palindrome(string)
    status = "✓ Palindrome" if is_pal else "✗ Not Palindrome"
    print(f"{string:35} | {status}")
