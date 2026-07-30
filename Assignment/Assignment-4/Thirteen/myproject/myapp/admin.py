from django.contrib import admin
from myapp.models import *
# Register your models here.

class displaysongs(admin.ModelAdmin):
    list_display = ['id','title','artist','duration']

admin.site.register(playlist,displaysongs)
