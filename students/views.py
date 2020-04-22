from django.shortcuts import render
from django.urls import reverse
from . models import Student
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
import json
from courses.models import Course
from utils.validators import phone_validator, name_validator, email_validator

context = {}

def get_students_list(request):
    # for searching field:
    if request.GET:
        name = request.GET.get('name')
        students = Student.objects.filter(name__contains=name)
    # for showing all student:
    else:
        students = Student.objects.all()
    courses = Course.objects.all()
    global context
    context = {'students': students, 'courses': courses, 'student_created_successfully': None}

    return render(request, 'students.html', context)


def delete_student(request):
    print(request.POST)
    try:
        student_id = request.POST.get('student_id')
        student = Student.objects.get(id=student_id)
        student.delete()
        return HttpResponseRedirect(reverse('students_list'))
    except Student.DoesNotExist:
        return HttpResponse("student doesn't exist")


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
    print(data_student)

    # name validation:
    if not name_validator(data_student.get('name')):
        return HttpResponse('The name is not valid!', status=400)
    # email validation:
    if not email_validator(data_student.get('email')):
        return HttpResponse('The email is not valid!')
    # phone number validation:
    if (data_student.get('phone') != '') and (not phone_validator(data_student.get('phone'))):
        return HttpResponse('The phone number is not valid', status=400)
    # check if a student has chosen any courses:
    if 'courses' in data_student:
        courses_id_list = request.POST.getlist('courses')
        del data_student['courses']
        student = Student.objects.create(**data_student)
        courses_list = Course.objects.filter(id__in=courses_id_list)
        student.courses.set(courses_list)
    else:
        Student.objects.create(**data_student)
    # add flag for modal window appearing:
    global context
    context['student_created_successfully'] = True

    return render(request, 'students.html', context)
