from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("reg",reg,name="reg"),
    path("home",home,name="home"),
    path("logout",logout_url,name="logout"),
    path("buyer",buyer,name="buyer"),
    path("seller",seller,name="seller")
]
