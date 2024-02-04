from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, ListView
from .forms import AddCommentForm
from django.contrib.auth.decorators import login_required
from .models import Books, BookReview, BookAuthor


class BookListView(View):
    def get(self, request):
        create_form = Books()
        context = {
            'form': create_form
        }
        return render(request, 'book_list.html', context=context)

    def post(self, request):
        form = Books(request.POST)
        if form.is_valid():
            book = form.save()

            return redirect(request, self.template_name, {'message': 'Book added successfully'})


class BookDetailView(DetailView):
    model = Books
    template_name = 'book_detail.html'
    context_name = 'book'

    def get(self, request, *args, **kwargs):
        book = self.get_object()
        return render(request, self.template_name, {'book': book})

    def post(self, request, *args, **kwargs):
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


@login_required(login_url='login')
def add_comment(request):
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('books')
    else:
        form = AddCommentForm()
    return render(request, 'add_comment.html', {'form': form})
