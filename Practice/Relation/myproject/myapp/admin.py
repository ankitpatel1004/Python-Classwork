from django.contrib import admin
from myapp.models import *

# Register your models here.

class displayproduct(admin.ModelAdmin):
    list_display = ['id','name','price','qty']

admin.site.register(Category)
admin.site.register(Product,displayproduct)
