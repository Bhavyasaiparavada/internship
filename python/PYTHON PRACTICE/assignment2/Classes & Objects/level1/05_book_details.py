class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


books = [Book("Python Basics", "R. Kumar", 500), Book("Learning Code", "M. Lee", 650)]
for book in books:
    print(book.title, book.author, book.price)