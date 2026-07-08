from django.contrib import admin
from myapp.models import *
# Register your models here.
admin.site.register(Product)

class CountryDisplay(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']
    list_filter=['name']

admin.site.register(Country,CountryDisplay)
admin.site.register(State)
admin.site.register(City)
