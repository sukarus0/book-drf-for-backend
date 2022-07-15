from django.urls import path, include
from .views import HelloAPI, booksAPI, bookAPI
from rest_framework import routers
from .views import BookViewSet

# urlpatterns = [
#         path("hello/", HelloAPI),
#         path("fbv/books/", booksAPI),
#         path("fbv/book/<int:bid>/", bookAPI),
# ]

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls
