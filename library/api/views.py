from rest_framework import mixins, viewsets

from .serializers import BookSerializer
from books.models import Book


class BookViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
