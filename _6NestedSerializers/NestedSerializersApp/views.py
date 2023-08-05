from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

from rest_framework import generics
# Using Django Filter
from django_filters.rest_framework import DjangoFilterBackend

# Using DRF's Filter
from rest_framework import filters
# Create your views here.

class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['firstName', 'lastName']

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['^firstName', '^lastName']

    # Ordering Filter
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['firstName', 'lastName', 'books']

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

