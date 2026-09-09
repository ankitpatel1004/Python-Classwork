from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("delete",delete_std,name="delete"),
    path("update",update_std,name="update")
]