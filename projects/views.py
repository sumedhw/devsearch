from curses.ascii import HT
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def projects(request):
    return render(request,'projects/projects.html')

def project(request,pk):
    return render(request,'projects/single-project.html')