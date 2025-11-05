from library import Library
from book import Book


def main():
    # Create some book objects
    b1 = Book("1984", "George Orwell", 1949)
    b2 = Book("The Alchemist", "Paulo Coelho", 1988)
    b3 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

    # Create a library and add the books
    lib = Library()
    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)

    # List all books
    print("\nAll books in the library:")
    lib.list_books()

    # Check out a book
    print("\nChecking out '1984'...")
    b1.checkout()

    # List again to see the change
    print("\nUpdated book list:")
    lib.list_books()

    # Find a book
    print("\nSearching for 'The Alchemist':")
    found = lib.find_book("The Alchemist")
    print(found)


if __name__ == "__main__":
    main()
