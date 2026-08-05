from django.urls import path
from myapp.views import *

urlpatterns = [
    path("sms",send_sms,name="sms")
]