# Update Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Updated book title to Nineteen Eighty-Four
