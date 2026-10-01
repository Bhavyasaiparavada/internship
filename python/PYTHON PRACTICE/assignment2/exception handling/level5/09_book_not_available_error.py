class BookNotAvailableError(Exception):
    pass


available_books = ["Python Basics", "Learning Math"]
try:
    book = input("Enter the book title to borrow: ")
    if book not in available_books:
        raise BookNotAvailableError("That book is not available.")
    print("You borrowed:", book)
except BookNotAvailableError as error:
    print(error)