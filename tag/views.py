from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Tag
from .se
# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer