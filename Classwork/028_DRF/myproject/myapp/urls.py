from django.urls import path
from myapp.views import *

urlpatterns = [
    path("create",create,name="create"),
    path("list",list,name="list"),
    path("update",update,name="update"),
    path("delete",delete,name="delete"),
    path("list-student",list_student,name="list-student"),
    path("create-student",create_student,name="create-student"),
    path("delete-student/<id>",delete_student,name="delete-student"),
    path("update-student/<id>",update_student,name="update-student")
]