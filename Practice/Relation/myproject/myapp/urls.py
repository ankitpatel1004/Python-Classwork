from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("create",create_product,name="create"),
    path("display",display_product,name="display"),
    path("delete",delete_product,name="delete"),
    path("update",update_product,name="update")
]

