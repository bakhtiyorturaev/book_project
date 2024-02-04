from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookReviewSerializer, BookAuthorSerializer, BooksSerializer, CustomerUserSerializer
from books.models import BookReview, BookAuthor, Books
from users.models import CustomUser


# Create your views here.


class BookReviewAPIView(APIView):
    def get(self, request):
        books_rev = BookReview.objects.all()
        serializer = BookReviewSerializer(books_rev, many=True)
        return Response(data=serializer.data)


class BookReviewDetailAPIView(APIView):
    def get(self, request, pk):
        book = BookReview.objects.get(pk=pk)
        serializer = BookReviewSerializer(book)
        return Response(data=serializer.data)


class BookAuthorAPIView(APIView):
    def get(self, request):
        book_author = BookAuthor.objects.all()
        serializer = BookAuthorSerializer(book_author, many=True)
        return Response(data=serializer.data)


class BookAPIView(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(data=serializer.data)


class BookDetailAPIView(APIView):
    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        serializer = BooksSerializer(book)
        return Response(data=serializer.data)


class CustomerUserAPIView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomerUserSerializer(users, many=True)
        return Response(data=serializer.data)


class CustomUserDetailAPIView(APIView):
    def get(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        serializer = CustomerUserSerializer(user)
        return Response(data=serializer.data)
