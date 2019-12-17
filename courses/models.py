import uuid
import random
from django.db import models
from users.models import UserProfile


def get_default_code(name):
    return str(name)[0] + str(random.random()*10**6)[:6]


class Course(models.Model):
    name = models.CharField(max_length=16, unique=True)
    code = models.CharField(max_length=8, default=get_default_code(name), unique=True)
    # code = models.UUIDField(default=str(name)[0] + uuid.uuid1().hex[:7], unique=True)
    users = models.ManyToManyField(UserProfile, blank=True, related_name='courses')

    def __str__(self):
        return f'{self.name}'
