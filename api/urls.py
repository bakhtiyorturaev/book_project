from django.urls import path
from .views import (BookReviewAPIView, BookReviewDetailAPIView, CustomerUserAPIView, CustomUserDetailAPIView,
                    BookAuthorAPIView, BookAPIView, BookDetailAPIView)

app_name = 'api'
urlpatterns = [
    path('book-reviews/', BookReviewAPIView.as_view(), name='book-reviews'),
    path('book-reviews/<int:pk>/', BookReviewDetailAPIView.as_view(), name='book-reviews-detail'),
    path('users/', CustomerUserAPIView.as_view(), name='users'),
    path('users/<int:pk>/', CustomUserDetailAPIView.as_view(), name='user-detail'),
    path('authors/', BookAuthorAPIView.as_view(), name='authors'),
    path('books/', BookAPIView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),


]