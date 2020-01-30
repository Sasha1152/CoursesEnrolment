from enum import Enum
from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=16)

    class Meta:
        db_table = "users_profiles"

    class UserStatus(Enum):
        active = 'Active'
        inactive = 'Inactive'

        @classmethod
        def choices(cls):
            return ((attr.name, attr.value) for attr in cls)

    status = models.CharField(max_length=8, choices=UserStatus.choices())

    def __str__(self):
        return f'{self.id}-{self.name}'
