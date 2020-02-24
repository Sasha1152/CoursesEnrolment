from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'email',
                    'phone',
                    'status',
                    )


admin.site.register(Student, StudentAdmin)
