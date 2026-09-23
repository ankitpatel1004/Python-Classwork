from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = "django_mongodb_backend.fields.ObjectIdAutoField"
    name = 'myapp'
