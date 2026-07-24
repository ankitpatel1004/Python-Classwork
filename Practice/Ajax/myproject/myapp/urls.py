from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("test",test,name="test"),
    path("search",search,name="search"),
    path("collages",collages,name="collages"),
    path("departments",departments,name="departments"),
    path("students",students,name="students")
]