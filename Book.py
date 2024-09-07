class Book:
    # Constructor to initialize a Book object with book_id, title, and author.
    def __init__(self, book_id, title, author):
        self.book_id = book_id  # Unique identifier for the book
        self.title = title  # Title of the book
        self.author = author  # Author of the book
        self.is_book_available = True  # Attribute to check if the book is available

    # Method to provide a string representation of the Book object.
    def __str__(self):
        return f"ID:{self.book_id}, Title:{self.title}, Author: {self.author}, Available: {self.is_book_available}"