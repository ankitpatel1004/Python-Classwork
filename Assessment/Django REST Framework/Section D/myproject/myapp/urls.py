from django.urls import path
from myapp.views import *

urlpatterns = [
     path("orders",PlaceOrderAPIView.as_view())
]