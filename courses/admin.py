from django.contrib import admin
from .models import Course


class UserInline(admin.TabularInline):
    model = Course.users.through


class CourseAdmin(admin.ModelAdmin):
    inlines = [
        UserInline,
    ]
    exclude = ('users',)
    list_display = ('id',
                    'name',
                    'code',
                    )


admin.site.register(Course, CourseAdmin)
