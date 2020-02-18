from django.db import models
from students.models import Student


class Course(models.Model):
    name = models.CharField(max_length=16, unique=True)
    code = models.CharField(max_length=6, unique=True)
    students = models.ManyToManyField(Student, blank=True, related_name='courses')

    class Meta:
        db_table = "courses"

    def __str__(self):
        return f'{self.name}'
