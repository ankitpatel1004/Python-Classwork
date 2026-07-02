from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class CustomeUserManager(BaseUserManager):

    def create_user(self,phone,password=None, **extra_fields):

        if not phone:
            raise ValueError('Phone number is required')

        user = self.model(
            phone=phone,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,phone,password=None,**extra_fields):

        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)

        return self.create_user(
            phone,
            password,
            **extra_fields
        )

