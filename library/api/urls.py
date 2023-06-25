from django.urls import include, path
from rest_framework import routers

from .views import BookViewSet, ReaderViewSet, ReservationViewSet

router = routers.DefaultRouter()
router.register(r"books", BookViewSet, basename="book")
router.register(r"readers", ReaderViewSet, basename="reader")
router.register(r"reservations", ReservationViewSet, basename="reservation")

urlpatterns = [
    path("v1/", include(router.urls)),
]
