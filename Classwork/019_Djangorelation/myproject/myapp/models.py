from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)

class Passport(models.Model):
    person = models.OneToOneField(Person,on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    pid = models.CharField(max_length=20)

class Category(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to="images",null=True)

    def total(self):
        return self.price*self.qty

class Book(models.Model):
    name = models.CharField(max_length=20)

class Author(models.Model):
    book = models.ManyToManyField(Book)
    name = models.CharField(max_length=20)
    
