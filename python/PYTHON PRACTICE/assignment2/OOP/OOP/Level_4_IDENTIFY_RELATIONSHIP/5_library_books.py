class Book:
    def __init__(self, title):
        self.title = title


class Library:
    def __init__(self):
        self.books = [Book("Math"), Book("Science")]


print("HAS-A: Library has Books")
print([book.title for book in Library().books])
