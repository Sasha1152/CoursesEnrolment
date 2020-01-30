from django.shortcuts import render
from . models import UserProfile


def get_users_list(request):
    users = UserProfile.objects.all()
    return render(request, 'users.html', {'users': users})
