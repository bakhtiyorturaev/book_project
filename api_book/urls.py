from django.urls import path
# from .views import BookReviewCRUD, BooksListCRUD
from .views import BookListAPIView, BooksDeleteUpdateDetailAPIView

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('reviews', BookReviewCRUD, basename='reviews')
# router.register('books', BooksListCRUD, basename='books')
# urlpatterns = router.urls


app_name = 'api_book'
urlpatterns = [
    # path('reviews/', BookReviewListAPIView.as_view(), name='book-reviews'),
    # path('reviews/<int:pk>/', BookReviewDeleteUpdateDetailAPIView.as_view(), name='book-reviews-detail'),
    # path('authors/', BookAuthorAPIView.as_view(), name='authors'),
    path('books/', BookListAPIView.as_view(), name='books-list'),
    path('books/<int:pk>/', BooksDeleteUpdateDetailAPIView.as_view(), name='book-list-detail'),

]
