from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("menu",menu,name="menu")
]