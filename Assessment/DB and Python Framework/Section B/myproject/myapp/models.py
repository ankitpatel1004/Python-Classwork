from django.db import models

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.username
        