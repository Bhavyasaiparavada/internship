def is_palindrome(value):
    text = str(value)
    return text == text[::-1]


print(is_palindrome(12321))
