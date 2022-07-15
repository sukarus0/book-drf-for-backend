from django.urls import path, include
from .views import HelloAPI, booksAPI, bookAPI

urlpatterns = [
        path("hello/", HelloAPI),
        path("fbv/books/", booksAPI),
        path("fbv/book/<int:bid>/", bookAPI),
]
