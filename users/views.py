from django.shortcuts import render
from django.urls import reverse
from . models import UserProfile
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
import json
from courses.models import Course


def get_users_list(request):
    # for searching field:
    if request.GET:
        name = request.GET.get('name')
        users = UserProfile.objects.filter(name__contains=name)
    # for showing all student:
    else:
        users = UserProfile.objects.all()
    courses = Course.objects.all()

    return render(request, 'users.html', {'users': users, 'courses': courses})


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
    if 'courses' in data_user:
        courses_id_list = request.POST.getlist('courses')
        del data_user['courses']
        user = UserProfile.objects.create(**data_user)
        courses_list = Course.objects.filter(id__in=courses_id_list)
        user.courses.set(courses_list)
    else:
        UserProfile.objects.create(**data_user)
    return HttpResponseRedirect(reverse('users_list'))
