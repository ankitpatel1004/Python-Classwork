from django.contrib import admin
from myapp.models import *

# Register your models here.

class displayuserdetails(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','role','phone','address','age']

admin.site.register(Role)
admin.site.register(CustomUser,displayuserdetails)
