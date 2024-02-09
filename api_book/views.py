from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import BookReviewSerializer, BookAuthorSerializer, BookSerializer
from books.models import BookReview, BookAuthor, Books


# Create your views here.


# BOOK_REVIEWS
# viewsets
# class BookReviewCRUDViewSet(viewsets.ModelViewSet):
#     # permission_classes = [IsAuthenticated, ]
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all().order_by('-create_at')
#     lookup_field = 'pk'

# generic
# class BookReviewListGeneric(generics.ListCreateAPIView):
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all().order_by('created_at')
#     lookup_field = 'pk'

# APIView
# class BookReviewListAPIView(APIView):
#     def get(self, request):
#         books_review = BookReview.objects.all()
#         paginator = PageNumberPagination()
#         page_obj = paginator.paginate_queryset(books_review, request)
#         serializer = BookReviewSerializer(page_obj, many=True)
#         return paginator.get_paginated_response(data=serializer.data)
#
#     def post(self, request):
#         serializer = BookReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# generic detail
# class BookReviewDeleteUpdateDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = [IsAuthenticated, ]
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all()
#     lookup_field = 'pk'

# APIView
# class BookReviewDeleteUpdateDetailAPIView(APIView):
#     def get(self, request, pk):
#         book_review = BookReview.objects.get(pk=pk)
#         serializer = BookReviewSerializer(book_review)
#         return Response(data=serializer.data)
#
#     def delete(self, request, pk):
#         book_review = BookReview.objects.get(pk=pk)
#         book_review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def put(self, request, pk):
#         book_review = BookReview.objects.get(pk=pk)
#         serializer = BookReviewSerializer(instance=book_review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk):
#         book_review = BookReview.objects.get(pk=pk)
#         serializer = BookReviewSerializer(instance=book_review, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#


# BOOK_AUTHOR
# APIView
# class BookAuthorAPIView(APIView):
#     def get(self, request):
#         book_author = BookAuthor.objects.all()
#         serializer = BookAuthorSerializer(book_author, many=True)
#         return Response(data=serializer.data)
#
#
#


# BOOKS
# viewset
# class BooksListCRUD(viewsets.ModelViewSet):
#     # permission_classes = [IsAuthenticated]
#     serializer_class = BookSerializer
#     queryset = Books.objects.all().order_by('-create_at')
#     lookup_field = 'pk'

# generic
# class BookListAPIViews(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = BookSerializer
#     queryset = Books.objects.all().order_by('-create_at')
#     lookup_field = 'pk'


# APIView
class BookListAPIView(APIView):
    def get(self, request):
        books = Books.objects.all()
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(page_obj, many=True)
        return paginator.get_paginated_response(data=serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


APIView


class BooksDeleteUpdateDetailAPIView(APIView):
    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(data=serializer.data)

    def delete(self, request, pk):
        book = Books.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        book = Books.objects.get(pk=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        book = BookReview.objects.get(pk=pk)
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
