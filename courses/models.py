import random
from django.db import models
from users.models import UserProfile


class Course(models.Model):
    name = models.CharField(max_length=16, unique=True)
    code = models.CharField(max_length=6, unique=True)
    users = models.ManyToManyField(UserProfile, blank=True, related_name='courses')

    class Meta:
        db_table = "courses"

    def __str__(self):
        return f'{self.name}'
