from Library import Library
from Book import Book
from Member import Member

# Creating Library Instance
library = Library()

# Fetch books from Open Library API and add them to the library
library.fetch_books_from_open_library(query="Python programming", max_results=5)

# Display books to verify they were added
library.display_books()

# Create some members
members = [
    Member(member_id=i, name=name) for i, name in enumerate([
        "Alice Johnson", "Bob Smith", "Charlie Brown", "James Gadonfini", 
        "Riccardo Calafiorri", "Jurrien Timber", "William Saliba", 
        "Gabriel Maghalese", "Kai Harvertz", "David Raya"], start=1)
]

# Add members to the library, checking for duplicates
for member in members:
    if member not in library.member:
        library.add_member(member)
    else:
        print(f"Member '{member.name}' already exists in the library system.")

# Display members
library.display_members()

member = members[0]  # The first member in the list
book_to_borrow = library.books[0]  # The first book in the library

# Display initial state
print("\nBefore borrowing:")
print(member)
print(book_to_borrow)

# Member attempts to borrow a book
member.borrow_book(book_to_borrow)

print("\n")
# Display books to verify they were lended
library.display_books()

print("\n")
#Member attempts to return borrowed book
member.return_book(book_to_borrow)

# Display state after returning
print("\nAfter returning:")
print(member)
print(book_to_borrow)

print("\n")
library.display_books()




                 