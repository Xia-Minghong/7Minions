from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Organizer
from .serializers import OrganizerSerializer


# provided: [GET].list(), [GET].retrieve(), [POST].create(), [PUT].update(), and [DELETE].destroy()

# Create your views here.
class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer



# Get organizer
# GET:  http://127.0.0.1:8000/organizers/1
