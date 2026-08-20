class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages


books = [
    Book("The Alchemist", "Paulo Coelho", 450, 208),
    Book("Pride and Prejudice", "Jane Austen", 550, 432),
    Book("Wings of Fire", "A. P. J. Abdul Kalam", 300, 180),
]

for book in books:
    print("Title:", book.title)
    print("Author:", book.author)
    print("Price: Rs.", book.price)
    print("Pages:", book.pages)
    print()
