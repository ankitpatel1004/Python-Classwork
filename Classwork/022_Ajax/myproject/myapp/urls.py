from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("test",test,name="test"),
    path("search",search,name="search"),
    path("countries",countries,name="countries"),
    path("states",states,name="states"),
    path("cities",cities,name="cities")
]
