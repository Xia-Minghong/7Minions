from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Event
from .serializers import EventSerializer

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer





# View all events
# GET:  http://127.0.0.1:8000/events/

# View an event
# GET:  http://127.0.0.1:8000/events/1/

# Create an event
# POST:  http://127.0.0.1:8000/events/
# {
#     "name": "UBS Career Talk",
#     "start_time": "18:30:00",
#     "end_time": "22:00:00",
#     "location": "TCT LT"
#     "description": "Gain first-hand understanding of what it's like to work in UBS."
# "organizer": "Career"
# }