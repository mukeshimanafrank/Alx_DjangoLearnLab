import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return [book.title for book in Book.objects.filter(author=author)]
    except Author.DoesNotExist:
        return []


def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return [book.title for book in library.books.all()]
    except Library.DoesNotExist:
        return []


def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian.name
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


if __name__ == "__main__":
    print("Books by 'John Smith':", books_by_author("John Smith"))
    print("Books in 'Central Library':", books_in_library("Central Library"))
    print("Librarian for 'Central Library':", librarian_for_library("Central Library"))
