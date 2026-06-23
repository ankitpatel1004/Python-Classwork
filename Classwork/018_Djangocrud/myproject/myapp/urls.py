from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("create",add_student,name="create"),
    path("display",display,name="display"),
    path("delete",delete_student,name="delete"),
    path("upate",update,name="update")
]