from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save()
