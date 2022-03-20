from django.contrib import admin

from book_app.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
