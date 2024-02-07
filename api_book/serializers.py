from rest_framework import serializers
from books.models import BookReview, BookAuthor, Books
from api_user.serializer import CustomUserSerializer


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class BookReviewSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    book_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BookReview
        fields = ['comment', 'star_given', 'user', 'book', 'user_id', 'book_id']


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = '__all__'

