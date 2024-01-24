from django.contrib import admin
from .models import Books, BookAuthor, BookReview, Author


class BookAuthorModel(admin.ModelAdmin):
    search_fields = ['book__title', 'author__name']
    list_display = ['get_book_title', 'get_author_name']

    def get_book_title(self, obj):
        return obj.book.title
    get_book_title.short_description = 'Book Title'

    def get_author_name(self, obj):
        return obj.author.name
    get_author_name.short_description = 'Author Name'


class BookModelAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']


admin.site.register(BookAuthor, BookAuthorModel)
admin.site.register(Books, BookModelAdmin)
admin.site.register(Author)
admin.site.register(BookReview)
