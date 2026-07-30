from django.db import models

# Create your models here.

class playlist(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    