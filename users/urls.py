from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_users_list, name='users_list'),
]
