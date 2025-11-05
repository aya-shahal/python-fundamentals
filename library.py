class Library:
    def __init__(self):
        self.collection = []

    def add_book(self, book):
        self.collection.append(book)

    def list_books(self):
        for book in self.collection:
            print(book)

    def find_book(self, title):
        for book in self.collection:
            if book.title.lower() == title.lower():
                return book
        return None