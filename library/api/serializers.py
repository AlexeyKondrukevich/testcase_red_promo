from datetime import timedelta

from books.models import Book, Reader, Reservation
from rest_framework import serializers

from library.settings import MAX_RESERVE_PERIOD


class BookSerializer(serializers.ModelSerializer):
    quantity_in_stock = serializers.SerializerMethodField()
    return_date = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "quantity",
            "quantity_in_stock",
            "return_date",
        )

    def get_quantity_in_stock(self, obj):
        return obj.quantity - obj.reserved.all().count()

    def get_return_date(self, obj):
        if self.get_quantity_in_stock(obj) == 0:
            last_reservation = obj.reserved.filter(status="RES").latest("date")
            book_return_date = last_reservation.date + timedelta(
                days=MAX_RESERVE_PERIOD
            )
            return book_return_date if last_reservation else None


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = ("status",)
