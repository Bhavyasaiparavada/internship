# Question 3: Create a Book class using __init__() and a method to display book information.

class Book:
    def __init__(self, title, author, isbn, pages, publication_year, price):
        """Initialize book attributes"""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages
        self.publication_year = publication_year
        self.price = price
    
    def display_info(self):
        """Display book information"""
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Pages: {self.pages}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Price: ${self.price:,.2f}")
        print("-" * 50)
    
    def display_brief_info(self):
        """Display brief book information"""
        print(f"{self.title} by {self.author} ({self.publication_year}) - ${self.price}")
    
    def get_book_age(self, current_year=2024):
        """Get the age of the book"""
        age = current_year - self.publication_year
        return age
    
    def apply_discount(self, discount_percentage):
        """Apply discount to book price"""
        discount_amount = (self.price * discount_percentage) / 100
        discounted_price = self.price - discount_amount
        print(f"Original Price: ${self.price:,.2f}")
        print(f"Discount ({discount_percentage}%): ${discount_amount:,.2f}")
        print(f"Final Price: ${discounted_price:,.2f}")
        return discounted_price


# Create book objects using __init__()
print("BOOK LIBRARY\n")

book1 = Book("Python Programming", "Guido van Rossum", "ISBN-001", 450, 2020, 49.99)
book2 = Book("Data Science Handbook", "Jake VanderPlas", "ISBN-002", 600, 2021, 59.99)
book3 = Book("Web Development", "Kyle Simpson", "ISBN-003", 520, 2019, 44.99)
book4 = Book("Machine Learning Guide", "Andrew Ng", "ISBN-004", 700, 2022, 69.99)
book5 = Book("Cloud Computing Basics", "Arjun Singh", "ISBN-005", 380, 2023, 39.99)

# Display detailed information
print("DETAILED BOOK INFORMATION")
print("=" * 50)
book1.display_info()
book2.display_info()
book3.display_info()

# Display brief information
print("\nBRIEF BOOK LIST")
print("=" * 50)
book1.display_brief_info()
book2.display_brief_info()
book3.display_brief_info()
book4.display_brief_info()
book5.display_brief_info()

# Get book age
print("\n\nBOOK AGE INFORMATION")
print("=" * 50)
print(f"{book1.title} - Age: {book1.get_book_age()} years")
print(f"{book2.title} - Age: {book2.get_book_age()} years")
print(f"{book3.title} - Age: {book3.get_book_age()} years")
print(f"{book4.title} - Age: {book4.get_book_age()} years")
print(f"{book5.title} - Age: {book5.get_book_age()} years")

# Apply discount
print("\n\nDISCOUNT CALCULATION")
print("=" * 50)
print(f"\n{book1.title}:")
book1.apply_discount(15)

print(f"\n{book4.title}:")
book4.apply_discount(20)
