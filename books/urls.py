from django.urls import path
from .views import BookListView, BookDetailView, BookAuthorListView, BookReviewListView, BookReviewDetailView, add_comment

app_name = 'books'

urlpatterns = [
    path('book-list/', BookListView.as_view(), name='book-list'),
    path('book-detail/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('bookauthor-list/', BookAuthorListView.as_view(), name='bookauthor-list'),
    path('bookreview-list/', BookReviewListView.as_view(), name='bookreview-list'),
    path('bookreview-detail/<int:pk>/', BookReviewDetailView.as_view(), name='bookreview-detail'),
    path('add/comment/', add_comment, name='add_comment'),

    # Add more URLs as needed
]
