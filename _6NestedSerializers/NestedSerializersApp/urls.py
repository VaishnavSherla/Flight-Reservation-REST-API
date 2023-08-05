from .views import AuthorListView, AuthorDetailView, BookListView, BookDetailView

from django.urls import path

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author'),
    
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book'),
]