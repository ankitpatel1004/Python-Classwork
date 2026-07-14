from django.contrib import admin
from myapp.models import *

# Register your models here.

class StudentDisplay(admin.ModelAdmin):
    list_display = ['id','name','email','age']

admin.site.register(Student,StudentDisplay)
