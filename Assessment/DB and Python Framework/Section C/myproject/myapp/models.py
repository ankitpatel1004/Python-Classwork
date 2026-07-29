from django.db import models

# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.username