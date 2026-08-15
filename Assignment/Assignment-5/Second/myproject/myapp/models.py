from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    rating = models.FloatField()

    def __str__(self):
        return self.name