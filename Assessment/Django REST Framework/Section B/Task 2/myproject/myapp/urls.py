from django.urls import path,include
from myapp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("items",MenuItemViewSet,basename='item')

router.register("categories",CategoryViewSet,basename='category')

urlpatterns = [
    path("",include(router.urls)),
]
