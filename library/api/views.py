from books.models import Book, Reader, Reservation
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .serializers import (BookSerializer, ReaderSerializer,
                          ReservationSerializer)


class BookViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReaderViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class ReservationViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        book = serializer.validated_data["book"]
        if (
            book.quantity
            - Reservation.objects.filter(
                book=serializer.validated_data["book"]
            ).count()
            > 0
        ):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        return Response(
            {"content": "Unfortunately, the book is over"},
            status=status.HTTP_400_BAD_REQUEST,
        )
