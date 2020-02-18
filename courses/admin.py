from django.contrib import admin
from .models import Course


class StudentInline(admin.TabularInline):
    model = Course.students.through


class CourseAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]
    exclude = ('students',)
    list_display = ('id',
                    'name',
                    'code',
                    )


admin.site.register(Course, CourseAdmin)
