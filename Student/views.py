from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    response_data = {}
    response_data['name'] = "test"
    response_data['age'] = 12
    return HttpResponse(json.dumps(response_data), content_type='application/json')

def signup(request):
    return HttpResponse()

def home(request):
    return render(request, "home.html", {})