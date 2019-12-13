from django.db import models
from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=16)
    code = models.CharField(max_length=16)
    users = models.ManyToManyField(User, blank=True, related_name='courses')
