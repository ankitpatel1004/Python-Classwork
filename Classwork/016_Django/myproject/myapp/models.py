from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    age = models.IntegerField()

class Product(models.Model):
    p_name = models.CharField(max_length=50)
    p_price = models.IntegerField()
    p_quantity = models.IntegerField()
    p_brand = models.CharField(max_length=50,default="Santoor")
    p_description = models.CharField(max_length=100,null=True)