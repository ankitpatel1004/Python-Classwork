from django.urls import path
from myapp.views import *

urlpatterns = [
    path("reg",get_reg,name="reg"),
    path("user",get_user,name="user"),
    path("admin",get_admin,name="admin"),
    path("normal",get_normal,name="normal")
]