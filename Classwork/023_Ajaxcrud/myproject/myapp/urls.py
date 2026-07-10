from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("register",register,name="register"),
    path("display",display,name="display"),
    path("search",search,name="search"),
    path("delete",delete_student,name="delete"),
    path("retrive",retrive,name="retrive"),
    path("update",update_student,name="update")
]