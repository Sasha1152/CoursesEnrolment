from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_users_list, name='users_list'),
    path('delete', views.delete_user, name='delete_user'),
    path('update', views.update_user, name='update_user'),
    path('create', views.create_user, name='create_user')
]
