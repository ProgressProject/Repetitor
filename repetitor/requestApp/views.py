from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from django.views.generic import View

from .forms import StudentForm


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
    return render(request, 'requestApp/students_list.html', context={'students': students})


class StudentCreate(View):
    def get (self, request):
        form = StudentForm()
        return render(request, 'requestApp/student_create.html', context={'form' : form})

    def post(self, request):
        bound_form = StudentForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
        return render(request, 'requestApp/student_create.html', context={'form': bound_form})
