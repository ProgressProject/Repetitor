from django.shortcuts import render, redirect
from django.http import HttpResponse


def info(request):
    return render(request, 'requestApp/info_course.html')

# Create your views here.
