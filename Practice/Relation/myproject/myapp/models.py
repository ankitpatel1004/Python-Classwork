from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
