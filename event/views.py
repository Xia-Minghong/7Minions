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
#     "name": 2,
#     "content": "haihui",
#     "rating": 4
# }