from .models import Book
from .serializers import BookSerializer
from rest_framework import generics


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
