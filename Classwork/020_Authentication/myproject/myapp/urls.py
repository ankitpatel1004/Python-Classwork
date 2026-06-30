from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("reg",reg,name="reg"),
    path("home",home,name="home"),
    path("logout",user_logout,name="logout")
]