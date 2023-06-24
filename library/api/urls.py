from django.urls import include, path
from rest_framework import routers

from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r"books", BookViewSet, basename="book")

urlpatterns = [
    path("v1/", include(router.urls)),
]
