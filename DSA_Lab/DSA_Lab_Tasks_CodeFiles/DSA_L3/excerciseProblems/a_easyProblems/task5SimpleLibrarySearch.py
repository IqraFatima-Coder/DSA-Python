# Problem 5: Simple Library Search
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)

    def search_book(self, book_name):
        return book_name in self.books

    def view_books(self):
        print("Books in Library:", self.books)

# Testing Library Search
library = Library()
books = ["Python Basics", "Data Science Handbook", "Machine Learning Guide"]
for book in books:
    library.add_book(book)

library.view_books()
search_query = "Data Science Handbook"
print(f"Is '{search_query}' available?:", library.search_book(search_query))
