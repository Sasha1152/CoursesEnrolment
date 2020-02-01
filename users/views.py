from django.shortcuts import render
from . models import UserProfile
from django.http import HttpResponse
import json


def get_users_list(request):
    if request.GET:
        name = request.GET.get('name')
        users = UserProfile.objects.filter(name__contains=name)
    else:
        users = UserProfile.objects.all()

    return render(request, 'users.html', {'users': users})