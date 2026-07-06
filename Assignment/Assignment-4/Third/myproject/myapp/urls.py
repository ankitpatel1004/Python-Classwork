from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",base,name="base"),
    path("explore",explore,name="explore"),
    path("profile",profile,name="profile")
]