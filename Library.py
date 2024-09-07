import requests
from Book import Book

class Library:
    def __init__(self):
        self.books = []
        self.member = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from the library.")
        else:
            print(f"Book '{book.title}' not found in the library.")

    def add_member(self, member):
        self.member.append(member)
        print(f"Member '{member.name}' added to the Library system.")

    def remove_member(self, member):
        if member in self.member:
            self.member.remove(member)
            print(f"Member '{member.name}' removed from the library system.")
        else:
            print(f"Member '{member.name}' not found in the library system.")

    def display_books(self):
        print("Available books in the library:")
        for book in self.books:
            print(book)

    def display_members(self):
        print("Library members:")
        for member in self.member:
            print(member)
            
    def fetch_books_from_open_library(self, query, max_results=5):
        """
        Fetches books from Open Library API based on a search query and adds them to the library.
        """
        api_endpoint = "https://openlibrary.org/search.json"
        params = {
            'q': query,
            'limit': max_results
        }

        try:
            response = requests.get(api_endpoint, params=params)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            
            books_data = response.json()
            docs = books_data.get('docs', [])
            
            for item in docs:
                title = item.get('title', 'No Title')
                authors = item.get('author_name', ['Unknown Author'])
                book_id = item.get('key', '').replace('/works/', '')
                
                # Only add book if title is present
                if title:
                    book = Book(book_id=book_id, title=title, author=', '.join(authors))
                    self.add_book(book)
                else:
                    print("Book without title encountered and skipped.")
                    
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")


