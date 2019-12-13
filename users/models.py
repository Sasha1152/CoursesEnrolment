from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    status = models.CharField(max_length=8, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return f'{self.id}-{self.name}'
