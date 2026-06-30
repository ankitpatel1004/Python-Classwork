from django.contrib import admin
from myapp.models import *

# Register your models here.

admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Book)
admin.site.register(Author)