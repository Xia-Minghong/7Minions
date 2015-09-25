from django.shortcuts import render
from student.models import *
from django.http import HttpResponse
from django.core import serializers
import json

# Create your views here.
def index(request):
    return HttpResponse("1")

def signup(request, matric_no, name):
    new_student = Student(matric_no=matric_no, name=name)
    new_student.save()
    return HttpResponse(json.dumps(serializers.serialize("json", [new_student])), content_type="application/json")

def login(request):
    return HttpResponse(0)