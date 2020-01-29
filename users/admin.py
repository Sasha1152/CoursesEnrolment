from django.contrib import admin
from .models import UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'email',
                    'phone',
                    'status',
                    )


admin.site.register(UserProfile, UserAdmin)
