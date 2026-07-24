from django.contrib import admin
from myapp.models import *

# Register your models here.
admin.site.register(Product)

class CollageDisplay(admin.ModelAdmin):
    list_display = ['id','name']
    # search_fields = ['name']
    # list_filter=['name']

admin.site.register(Collage)
admin.site.register(Department)
admin.site.register(Student)