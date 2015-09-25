from django.shortcuts import render
from student.models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("1")

def signup(request, matric_no, name):
    return HttpResponse(matric_no)

def login(request):
    return HttpResponse(0)