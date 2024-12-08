from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"Author named '{author_name}' does not exist."

# Query 2: List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return f"Library named '{library_name}' does not exist."

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        return f"Library named '{library_name}' does not exist."
    except Librarian.DoesNotExist:
        return f"No librarian found for library '{library_name}'."

# Sample usage
if __name__ == "__main__":
    author_name = "John Doe"
    library_name = "Central Library"

    # Query all books by a specific author
    books_by_author = get_books_by_author(author_name)
    print(f"Books by {author_name}: {books_by_author}")

    # List all books in a library
    books_in_library = list_books_in_library(library_name)
    print(f"Books in {library_name}: {books_in_library}")

    # Retrieve the librarian for a library
    librarian_for_library = get_librarian_for_library(library_name)
    print(f"Librarian for {library_name}: {librarian_for_library}")