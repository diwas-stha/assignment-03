'''
Implement a simple program to interact with the library catalog system. Create a Python class Book to represent a single book with 
attributes: Title, Author, ISBN, Genre, Availability (whether the book is available for
borrowing or not). 

Create another Python class LibraryCatalog to manage the collection of books with following functionalities:
- Add books by storing each book objects (Hint: Create an empty list in constructor
and store book objects)
- get book details and get all books from the list of objects
'''


class Book:
    def __init__(self, title, author, isbn, genre, availability=True):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._genre = genre
        self._availability = availability

    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}, Genre: {self._genre}, Availability: {self._availability}"


class Library_Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book._title == title:
                return book

    def get_all_books(self):
        return self.books


if __name__ == "__main__":
    library = Library_Catalog()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald",
                 "9780743273565", "Classic")
    book2 = Book("To Kill a Mockingbird", "Harper Lee",
                 "9780061120084", "Fiction")
    book3 = Book("1984", "George Orwell", "9780451524935",
                 "Science Fiction", availability=False)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    book_title = "1984"

    result_book = library.find_book_by_title(book_title)

    if result_book:
        print("Book Found:", result_book)
    else:
        print(f"Book by title {book_title} not found")

    all_books = library.get_all_books()
    print("/n All the books in library catalog are: ")
    for book in all_books:
        print(book)
