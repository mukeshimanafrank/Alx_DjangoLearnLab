# Create Book

from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# <Book: 1984>
