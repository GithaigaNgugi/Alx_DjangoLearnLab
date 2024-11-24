from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from .models import Book
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Serialize the data using BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing CRUD operations on Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    ...
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
