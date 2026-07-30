from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from myapp.manager import *

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=15,unique=True)
    address = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True,null=True)

    username = None
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    