from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Query all books by a specific author."""
    return Book.objects.filter(author__name=author_name)

def get_books_in_library(library_name):
    """List all books in a library."""
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None
