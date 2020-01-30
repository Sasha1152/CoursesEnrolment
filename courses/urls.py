from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_courses_list, name='courses_list'),
]