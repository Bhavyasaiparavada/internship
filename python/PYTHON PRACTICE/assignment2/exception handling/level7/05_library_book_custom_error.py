class BookNotAvailableError(Exception):
    pass


class Library:
    def __init__(self, books):
        self.books = books

    def borrow(self, book):
        if book not in self.books:
            raise BookNotAvailableError("That book is not available.")
        self.books.remove(book)
        return book


library = Library(["Python Basics", "Math Book"])
try:
    print("Borrowed:", library.borrow("Python Basics"))
except BookNotAvailableError as error:
    print(error)