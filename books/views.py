from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import Books, BookReview, BookAuthor


class BookListView(ListView):
    model = Books
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get(self, request, *args, **kwargs):
        books = self.get_queryset()
        return render(request, self.template_name, {'books': books})

    def post(self, request, *args, **kwargs):
        # Handle post request logic
        # For example, create a new book based on the form data
        # Redirect to the book list page or display a success message
        return render(request, self.template_name, {'message': 'Book added successfully'})


class BookDetailView(DetailView):
    model = Books
    template_name = 'book_detail.html'
    context_name = 'book'

    def get(self, request, *args, **kwargs):
        book = self.get_object()
        return render(request, self.template_name, {'book': book})

    def post(self, request, *args, **kwargs):
        # Handle post request logic (if needed)
        return render(request, self.template_name, {'message': 'Post request for book detail view'})


class BookAuthorListView(ListView):
    model = BookAuthor
    template_name = 'books/bookauthor_list.html'
    context_name = 'bookauthors'

    def get(self, request, *args, **kwargs):
        bookauthors = self.get_queryset()
        return render(request, self.template_name, {'bookauthors': bookauthors})

    def post(self, request, *args, **kwargs):
        # Handle post request logic (if needed)
        return render(request, self.template_name, {'message': 'Post request for bookauthor list view'})


class BookReviewListView(ListView):
    model = BookReview
    template_name = 'books/bookreview_list.html'
    context_name = 'bookreviews'

    def get(self, request, *args, **kwargs):
        bookreviews = self.get_queryset()
        return render(request, self.template_name, {'bookreviews': bookreviews})

    def post(self, request, *args, **kwargs):
        # Handle post request logic (if needed)
        return render(request, self.template_name, {'message': 'Post request for bookreview list view'})


class BookReviewDetailView(DetailView):
    model = BookReview
    template_name = 'books/bookreview_detail.html'
    context_object_name = 'bookreview'

    def get(self, request, *args, **kwargs):
        bookreview = self.get_object()
        return render(request, self.template_name, {'bookreview': bookreview})

    def post(self, request, *args, **kwargs):
        # Handle post request logic (if needed)
        return render(request, self.template_name, {'message': 'Post request for bookreview detail view'})
