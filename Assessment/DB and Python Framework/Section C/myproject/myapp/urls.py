from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",profile_list,name="profile_list"),
    path("create",create_profile,name="create"),
    path("export",export_profiles,name="export")
]
