from django.contrib import admin
from myapp.models import *
# Register your models here.
admin.site.register(Dept)
admin.site.register(Enrollment)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Marks)