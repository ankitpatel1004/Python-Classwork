from django.urls import path
from myapp.views import *

urlpatterns = [
    path("reg",reg,name="reg"),
    path("student",get_student,name="student"),
    path("faculty",get_faculty,name="faculty"),
    path("normal",get_normal,name="normal"),
]
