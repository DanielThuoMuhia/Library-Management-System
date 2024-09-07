class Member:
    # Constructor to initialize a Member object with member_id and name.
    def __init__(self, member_id, name):
        self.member_id = member_id  # Unique identifier for the member
        self.name = name  # Name of the member
        self.borrowed_books = []  # List to store borrowed books

    # Method to borrow a book if it is available.
    def borrow_book(self, book):
        if book.is_book_available:  # Check if the book is available to borrow
            self.borrowed_books.append(book)  # Add the book to the member's borrowed books list
            book.is_book_available = False  # Mark the book as not available
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently not available.")  # Inform that the book is not available

    # Method to return a borrowed book.
    def return_book(self, book):
        if book in self.borrowed_books:  # Check if the book is in the member's borrowed books list
            self.borrowed_books.remove(book)  # Remove the book from the borrowed list
            book.is_book_available = True  # Mark the book as available
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")  # Inform that the member did not borrow the book

    # Method to provide a string representation of the Member object.
    def __str__(self) -> str:
        # Returns the member details and a list of borrowed books' titles
        return f"Member ID: {self.member_id}, Name: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"
         