from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student


def info(request):
    return render(request, 'requestApp/info_course.html')

# Create your views here.
def contacts(request):
    return render(request, 'requestApp/contacts.html')

def reviews(request):
    return render(request, 'requestApp/reviews.html')

def students_list(request):
    """ выводит список всех оставивших заявку, студентов """
    students = Student.objects.all()
    return render(request, 'blog/students_list.html', context={'students': students})
