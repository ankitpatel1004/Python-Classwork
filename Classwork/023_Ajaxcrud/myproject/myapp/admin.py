from django.contrib import admin
from myapp.models import *
# Register your models here.

class displaystudent(admin.ModelAdmin):
    list_display = ['id','name','email','age']

admin.site.register(Student,displaystudent)