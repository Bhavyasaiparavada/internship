class Number:
    def __init__(self, value):
        self.value = value

    def is_even(self):
        return self.value % 2 == 0

    def is_odd(self):
        return self.value % 2 != 0

    def is_prime(self):
        if self.value < 2:
            return False
        for number in range(2, self.value):
            if self.value % number == 0:
                return False
        return True

    def is_palindrome(self):
        text = str(self.value)
        return text == text[::-1]


number = Number(131)
print("Even:", number.is_even())
print("Odd:", number.is_odd())
print("Prime:", number.is_prime())
print("Palindrome:", number.is_palindrome())