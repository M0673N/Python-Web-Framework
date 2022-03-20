from django.urls import path

from book_app.books.views import ListBooksView, DetailBookView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name="books-all"),
    path('books/<int:pk>', DetailBookView.as_view(), name="books-detail")
]
