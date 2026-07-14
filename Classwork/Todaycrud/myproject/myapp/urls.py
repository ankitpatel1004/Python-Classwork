from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("create",add_student,name="create"),
    path("display",display,name="display"),
    path("delete",delete,name="delete"),
    path("update",update,name="update")
]
