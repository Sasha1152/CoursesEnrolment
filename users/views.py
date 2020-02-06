from django.shortcuts import render
from django.urls import reverse
from . models import UserProfile
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
import json


def get_users_list(request):
    if request.GET:
        name = request.GET.get('name')
        users = UserProfile.objects.filter(name__contains=name)
    else:
        users = UserProfile.objects.all()

    return render(request, 'users.html', {'users': users})


def delete_user(request):
    user_id = request.POST.get('user_id')
    user = UserProfile.objects.get(id=user_id)
    user.delete()
    return HttpResponseRedirect(reverse('users_list'))


def update_user(request):
    new_data_dict = request.POST.dict()
    user = UserProfile.objects.get(id=new_data_dict['user_id'])
    for key in new_data_dict:
        if key in vars(user):
            vars(user)[key] = new_data_dict[key]
    user.save()
    print(new_data_dict)
    return HttpResponseRedirect(reverse('users_list'))


def create_user(request):
    data_user = request.POST.dict()
    UserProfile.objects.create(**data_user)
    print(data_user)
    return HttpResponseRedirect(reverse('users_list'))
