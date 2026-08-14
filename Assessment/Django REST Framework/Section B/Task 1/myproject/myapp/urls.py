from django.urls import path
from myapp.views import *

urlpatterns = [
    path("categories",CategoryAPI.as_view())
]