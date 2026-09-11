from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("delete",delete_emp,name="delete"),
    path("update",update_emp,name="update")
]