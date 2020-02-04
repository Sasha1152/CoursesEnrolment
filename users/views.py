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
    print(user_id)
    user.delete()
    return HttpResponseRedirect(reverse('users_list'))

# def delete_user(request):
#     # data = json.loads(request.body.decode('utf-8'))
#     print('MYPRINT: ', request.POST.get('user_id'))
#     return HttpResponse(request.POST.get('user_id'))
