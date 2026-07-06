from django.urls import path
from playlists.views import *

urlpatterns = [
    path("",home,name="home"),
    path("music",music,name="music")
]