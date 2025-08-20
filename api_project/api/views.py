from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):  # Change here to ListAPIView
    queryset = Book.objects.all()
    serializer_class = BookSerializer
