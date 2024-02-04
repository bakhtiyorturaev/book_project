from rest_framework import serializers
from books.models import BookReview, BookAuthor, Books
from users.models import CustomUser
# BookList, BookDetail, ReviewDetail


class CustomerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class BookReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    book = serializers.CharField()

    class Meta:
        model = BookReview
        fields = '__all__'


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
