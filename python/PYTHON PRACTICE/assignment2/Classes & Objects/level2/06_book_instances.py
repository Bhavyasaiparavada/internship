class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages


books = [Book("Python Basics", "R. Kumar", 500, 200), Book("Web Design", "M. Lee", 650, 300)]
for book in books:
    print(book.title, book.author, book.price, book.pages)