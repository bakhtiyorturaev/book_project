from django.db import models
from django.contrib.auth import get_user_model


class Author(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'authors_table'


class Books(models.Model):
    title = models.CharField(max_length=100)
    pageCount = models.IntegerField(default=0)
    author = models.ManyToManyField(Author)
    description = models.TextField()
    image_book = models.ImageField(default='books_image/book_image.jpg', upload_to='media')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'books_table'


class BookAuthor(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default='deleted author')

    def __str__(self):
        return f"{self.book.title} {self.author.name}"

    def get_info(self):
        return f"{self.book.title} {self.author.name}"

    class Meta:
        db_table = 'book_author_table'


class BookReview(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title

    class Meta:
        db_table = 'review_table'

