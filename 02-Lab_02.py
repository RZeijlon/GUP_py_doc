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
    

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Book is available by default

    def mark_as_borrowed(self):
        
        self.available = False

    def mark_as_returned(self):
        
        self.available = True


class Library:
    

    def __init__(self):
        self.books = []

    def add_book(self, book):
       
        self.books.append(book)

    def borrow_book(self, isbn):
        
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.mark_as_borrowed()
                return True
        return False

    def return_book(self, isbn):
        
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.mark_as_returned()
                return True
        return False

# Example usage
library = Library()
book1 = Book("1984", "George Orwell", "1234567890")
library.add_book(book1)

library.borrow_book("1234567890")
library.return_book("1234567890")
