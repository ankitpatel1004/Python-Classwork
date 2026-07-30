from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
        path("register",register,name="register"),
    path('display',display_data,name="display"),
    path("delete",delete_song,name="delete"),
    path("retrive",retrive_data,name="retrive"),
    path("update",update_data,name='update')
]
