"""
Task:
Document a small library for managing a 
Book and Library system. The code includes 
two classes, and students will need to explain 
the functionality of each method and add comments.

Task:
Document the code using both comments and docstrings
for each class and method.
Ensure that comments explain the purpose of major 
code sections.
Use meaningful comments for algorithms 
(e.g., iterating over books to borrow or return).

"""

#code
class Book:
    """
    A class representing a book in a library.

    Attributes
    ----------
    title : str
        The title of the book.
    author : str
        The author of the book.
    isbn : str
        The ISBN of the book.
    available : bool
        A flag indicating whether the book is available.

    Methods
    -------
    mark_as_borrowed()
        Marks the book as not available.
    mark_as_returned()
        Marks the book as available.
    """

    def __init__(self, title:str, author:str, isbn:str):
        """
        Initializes a new book with the given title, author, and ISBN.

        Parameters
        ----------
        title: str
            The title of the book.
        author: str
            The author of the book.
        isbn: str
            The ISBN of the book.

        Variables
        ----------
        available: bool -> True
            A flag indicating whether the book is available
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Book is available by default

    def mark_as_borrowed(self):
        """
        Changes the availability of the book to False.
        """
        self.available = False

    def mark_as_returned(self):
        """
        Changes the availability of the book to True.
        """
        self.available = True


class Library:
    """
    A class representing a library that manages books.

    Attributes
    ----------
    books : list[Book]
        A list of books in the library.

    Methods
    -------
    add_book(book: Book)
        Adds a book to the library.
    borrow_book(isbn: str) -> bool
        Borrows a book from the library.
    return_book(isbn: str) -> bool
        Returns a borrowed book to the library.
    """

    def __init__(self):
        """
        Initializes a new library with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book to the library.

        Parameters
        ----------
        book: Book
            The book to add to the library.
        """
        self.books.append(book)

    def borrow_book(self, isbn):
        """
        Lets a user borrow a book from the library.

        Parameters
        ----------
        isbn: str
            The ISBN of the book to borrow.

        Returns
        -------
        bool
            True if the book was successfully borrowed, False otherwise
        """
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.mark_as_borrowed()
                return True
        return False

    def return_book(self, isbn):
        """
        Lets a user return a borrowed book to the library.

        Parameters
        ----------
        isbn: str
            The ISBN of the book to return.

        Returns
        -------
        bool
            True if the book was successfully returned, False otherwise
        """
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.mark_as_returned()
                return True
        return False

# Example usage (should be in a separate file)

# Create a example library object
library = Library()
# Create a example book object
book1 = Book("1984", "George Orwell", "1234567890")
# Add the book to the library
library.add_book(book1)
# Borrow the book from the library
library.borrow_book("1234567890")
# Return the borrowed book to the library
library.return_book("1234567890")
