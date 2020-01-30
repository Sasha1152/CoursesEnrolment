from django.shortcuts import render
from .models import Course


def get_courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})
