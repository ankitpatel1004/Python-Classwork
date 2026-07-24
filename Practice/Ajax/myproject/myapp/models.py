from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)

class Collage(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Department(models.Model):
    collage = models.ForeignKey(Collage,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)