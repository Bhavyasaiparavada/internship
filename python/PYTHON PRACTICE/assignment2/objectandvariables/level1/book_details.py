class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


books = [
    Book("The Alchemist", "Paulo Coelho", 400),
    Book("Wings of Fire", "A. P. J. Abdul Kalam", 350),
]

for book in books:
    print("Title:", book.title)
    print("Author:", book.author)
    print("Price: Rs.", book.price)
    print()
