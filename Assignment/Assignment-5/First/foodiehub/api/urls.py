from django.urls import path
from api.views import *

urlpatterns = [
    path("spotify",hello_spotify,name="spotify")
]