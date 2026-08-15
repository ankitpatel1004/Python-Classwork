from django.db import models

# Create your models here.

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    item = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.customer_name} - {self.item}"
        