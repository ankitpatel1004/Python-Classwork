from django.contrib import admin
from myapp.models import *
# Register your models here.

class ProductDisplay(admin.ModelAdmin):
    list_display = ['name','price','qty']

admin.site.register(Product,ProductDisplay)
