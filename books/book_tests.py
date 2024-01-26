from django.test import TestCase
from .views import Books
from django.urls import reverse

# Create your tests here.


class BookListTest(TestCase):
    def test_book_list(self):
        Books.objects.create(title='title1', price=1231, description='description1')
        Books.objects.create(title='title2', price=1232, description='description2')
        Books.objects.create(title='title3', price=1233, description='description3')

        books = Books.objects.all()

        book_list = self.client.get(reverse('books:book-list'))
        for book in books:
            self.assertContains(book_list, book.title)

    def test_book_detail(self):
        book = Books.objects.create(title='title1', price=1231, description='description1')
        url = reverse('books:book-detail', kwargs={'pk': book.pk})
        book_detail = self.client.get(url)
        self.assertContains(book_detail, book.title)