from django.contrib import admin
from myapp.models import *

# Register your models here.

# Customize Admin List View
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name','cuisine','rating']

    #search functionality
    search_fields = ['name','cuisine']

    #filter Restaurant using list_filter
    list_filter = ['cuisine',]
admin.site.register(Restaurant,RestaurantAdmin)