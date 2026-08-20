# Question 7: Create a Number class with methods to check whether a number is even, odd, prime, or palindrome.

class Number:
    def __init__(self, value=0):
        """Initialize number"""
        self.value = value
    
    def is_even(self, num=None):
        """Check if number is even"""
        n = num if num is not None else self.value
        return n % 2 == 0
    
    def is_odd(self, num=None):
        """Check if number is odd"""
        n = num if num is not None else self.value
        return n % 2 != 0
    
    def is_prime(self, num=None):
        """Check if number is prime"""
        n = num if num is not None else self.value
        
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def is_palindrome(self, num=None):
        """Check if number is palindrome"""
        n = num if num is not None else self.value
        num_str = str(abs(n))
        return num_str == num_str[::-1]
    
    def is_perfect_square(self, num=None):
        """Check if number is perfect square"""
        n = num if num is not None else self.value
        if n < 0:
            return False
        sqrt = int(n ** 0.5)
        return sqrt * sqrt == n
    
    def is_armstrong(self, num=None):
        """Check if number is Armstrong number"""
        n = num if num is not None else self.value
        if n < 0:
            return False
        
        digits = str(n)
        num_digits = len(digits)
        sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
        return sum_of_powers == n
    
    def get_factors(self, num=None):
        """Get all factors of a number"""
        n = num if num is not None else self.value
        if n <= 0:
            return []
        
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors
    
    def display_number_properties(self, num=None):
        """Display all properties of a number"""
        n = num if num is not None else self.value
        
        print(f"\n{'='*60}")
        print(f"NUMBER ANALYSIS: {n}")
        print(f"{'='*60}")
        print(f"Even: {'Yes' if self.is_even(n) else 'No'}")
        print(f"Odd: {'Yes' if self.is_odd(n) else 'No'}")
        print(f"Prime: {'Yes' if self.is_prime(n) else 'No'}")
        print(f"Palindrome: {'Yes' if self.is_palindrome(n) else 'No'}")
        print(f"Perfect Square: {'Yes' if self.is_perfect_square(n) else 'No'}")
        print(f"Armstrong Number: {'Yes' if self.is_armstrong(n) else 'No'}")
        factors = self.get_factors(n)
        if n > 0:
            print(f"Factors: {factors}")
            print(f"Number of Factors: {len(factors)}")
        print(f"{'='*60}\n")
    
    def analyze_number(self, num):
        """Analyze a number and print analysis"""
        self.value = num
        self.display_number_properties(num)


# Create number object
print("NUMBER PROPERTIES CHECKER\n")

number_obj = Number()

# Check individual properties
print("INDIVIDUAL PROPERTY CHECKS")
print("=" * 60)

# Check even/odd
print("\nEven/Odd Check:")
test_numbers = [10, 15, 20, 25]
for num in test_numbers:
    even = "Even" if number_obj.is_even(num) else "Odd"
    print(f"  {num}: {even}")

# Check prime
print("\nPrime Number Check:")
test_primes = [2, 3, 5, 10, 11, 15, 17, 20, 23]
for num in test_primes:
    is_prime = "Prime" if number_obj.is_prime(num) else "Not Prime"
    print(f"  {num}: {is_prime}")

# Check palindrome
print("\nPalindrome Number Check:")
test_palindromes = [11, 121, 131, 123, 1221, 9009]
for num in test_palindromes:
    is_pal = "Palindrome" if number_obj.is_palindrome(num) else "Not Palindrome"
    print(f"  {num}: {is_pal}")

# Check perfect squares
print("\nPerfect Square Check:")
test_squares = [1, 4, 9, 10, 16, 25, 30, 36]
for num in test_squares:
    is_square = "Perfect Square" if number_obj.is_perfect_square(num) else "Not Perfect Square"
    print(f"  {num}: {is_square}")

# Check Armstrong numbers
print("\nArmstrong Number Check:")
test_armstrong = [153, 370, 371, 407, 123, 100]
for num in test_armstrong:
    is_arm = "Armstrong" if number_obj.is_armstrong(num) else "Not Armstrong"
    print(f"  {num}: {is_arm}")

# Display detailed analysis
print("\n\nDETAILED NUMBER ANALYSIS")
print("=" * 60)

test_numbers_detailed = [17, 25, 121, 153]
for num in test_numbers_detailed:
    number_obj.display_number_properties(num)

# Get factors
print("\n\nFACTOR ANALYSIS")
print("=" * 60)
numbers_for_factors = [12, 20, 30, 36]
for num in numbers_for_factors:
    factors = number_obj.get_factors(num)
    print(f"\nFactors of {num}: {factors}")
    print(f"Total Factors: {len(factors)}")
    print(f"Sum of Factors: {sum(factors)}")

# Summary
print("\n\nNUMBER PROPERTIES SUMMARY")
print("=" * 60)
print(f"{'Number':<10} {'Even':<8} {'Odd':<8} {'Prime':<8} {'Palindrome':<12} {'Sq':<4} {'Arm':<4}")
print("-" * 65)

summary_numbers = [2, 7, 10, 11, 16, 17, 121, 153]
for num in summary_numbers:
    even = "✓" if number_obj.is_even(num) else ""
    odd = "✓" if number_obj.is_odd(num) else ""
    prime = "✓" if number_obj.is_prime(num) else ""
    palindrome = "✓" if number_obj.is_palindrome(num) else ""
    square = "✓" if number_obj.is_perfect_square(num) else ""
    armstrong = "✓" if number_obj.is_armstrong(num) else ""
    
    print(f"{num:<10} {even:<8} {odd:<8} {prime:<8} {palindrome:<12} {square:<4} {armstrong:<4}")
