class SearchService:
    def search(self, books, title):
        return title in books


class Library:
    def __init__(self):
        self.books = ["Math", "Science"]

    def find_book(self, service, title):
        return service.search(self.books, title)


library = Library()
print("Math found:", library.find_book(SearchService(), "Math"))
