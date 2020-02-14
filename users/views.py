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


# def get_user_courses(request):
#     user_id = request.POST.get('user_id')
#     user = UserProfile.objects.get(id=user_id)
#     courses = user.courses.all()
#     user_courses = [course.name for course in courses]
#     print(user_courses)
#     # return HttpResponse('OK')
#     return render(request, 'users.html', {'user_courses': user_courses})


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
    print(data_user)
    if 'courses' in data_user:
        courses = Course.objects.filter(id=data_user['courses'])
        print(courses)
    else:
        print('NO')
    # UserProfile.objects.create(**data_user)
    return HttpResponseRedirect(reverse('users_list'))
