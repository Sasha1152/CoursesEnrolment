from django.shortcuts import render
from django.urls import reverse
from . models import Student
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
import json
from courses.models import Course


def get_students_list(request):
    # for searching field:
    if request.GET:
        name = request.GET.get('name')
        students = Student.objects.filter(name__contains=name)
    # for showing all student:
    else:
        students = Student.objects.all()
    courses = Course.objects.all()

    return render(request, 'students.html', {'students': students, 'courses': courses})


def delete_student(request):
    student_id = request.POST.get('student_id')
    student = Student.objects.get(id=student_id)
    student.delete()
    return HttpResponseRedirect(reverse('students_list'))


def update_student(request):
    new_data_dict = request.POST.dict()
    student = Student.objects.get(id=new_data_dict['student_id'])
    for key in new_data_dict:
        if key in vars(student):
            vars(student)[key] = new_data_dict[key]
    student.save()
    print(new_data_dict)
    return HttpResponseRedirect(reverse('students_list'))


def create_student(request):
    data_student = request.POST.dict()
    if 'courses' in data_student:
        courses_id_list = request.POST.getlist('courses')
        del data_student['courses']
        student = Student.objects.create(**data_student)
        courses_list = Course.objects.filter(id__in=courses_id_list)
        student.courses.set(courses_list)
    else:
        Student.objects.create(**data_student)
    return HttpResponseRedirect(reverse('students_list'))
