from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("create",create,name="create"),
    path("display",display,name="display")
]