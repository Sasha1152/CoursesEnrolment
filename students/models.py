from enum import Enum
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(blank=True, max_length=18)

    class Meta:
        db_table = "students"

    class StudentStatus(Enum):
        active = 'Active'
        inactive = 'Inactive'

        @classmethod
        def choices(cls):
            return ((attr.name, attr.value) for attr in cls)

    status = models.CharField(max_length=8, choices=StudentStatus.choices())

    def __str__(self):
        return f'{self.id}-{self.name}'
