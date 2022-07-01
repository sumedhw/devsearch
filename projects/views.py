from curses.ascii import HT
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def projects(request):
    return HttpResponse("Projects list")

def project(request,pk):
    return HttpResponse(f"This is project {pk}")