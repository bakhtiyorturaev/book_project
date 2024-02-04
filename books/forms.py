from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import BookReview, Books


class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'pageCount', 'author', 'image_book', 'price']
        # exclude = ['create_at']

    def __init__(self, *args, **kwargs):
        super(UpdateBookForm, self).__init__(*args, **kwargs)


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = (
            'book', 'user', 'comment'
        )
