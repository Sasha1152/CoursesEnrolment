from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_students_list, name='students_list'),
    path('delete', views.delete_student, name='delete_student'),
    path('update', views.update_student, name='update_student'),
    path('create', views.create_student, name='create_student'),
]
