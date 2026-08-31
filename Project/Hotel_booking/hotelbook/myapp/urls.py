from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",home,name="home"),
    path("rooms",rooms,name="rooms"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
    path("login",login,name="login"),
    path("register",register,name="register"),
    path("logout",logout,name="logout"),
    path("search/",search_rooms,name="search_rooms")
]