from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    status = models.CharField(max_length=8, choices=[('active', 'Active'), ('inactive', 'Inactive')])
