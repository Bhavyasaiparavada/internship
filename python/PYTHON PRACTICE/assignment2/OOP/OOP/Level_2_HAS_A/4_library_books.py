class Book:
    def __init__(self, title):
        self.title = title


class Library:
    def __init__(self):
        self.books = [Book("Math"), Book("Science")]


library = Library()
for book in library.books:
    print(book.title)
