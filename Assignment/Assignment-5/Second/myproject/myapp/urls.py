from django.urls import path
from myapp.views import *

urlpatterns = [
    path("restaurant",RestaurantAPI.as_view()),
    path("restaurant/<id>",RestaurantAPIById.as_view())
]