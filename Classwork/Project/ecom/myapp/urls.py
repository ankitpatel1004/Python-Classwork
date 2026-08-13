from django.urls import path,include
from myapp.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(
    "categories",
    CategoryViewSet,
    basename="category"
)

router.register(
    "users",
    UserViewSet,
    basename="user"
)

urlpatterns = [
    path("", include(router.urls)),
]
