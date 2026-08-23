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

router.register("products",ProductViewSet,basename="product")

router.register("addresses",AddressViewSet,basename="address")

urlpatterns = [
    path("", include(router.urls)),
    path("carts",CartViewSet.as_view()),
    path("payment",payment,name="payment"),
]
