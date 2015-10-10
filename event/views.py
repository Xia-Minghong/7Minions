from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import list_route, detail_route
from organizer.models import Organizer
from rest_framework.response import Response

from rest_framework.decorators import detail_route
from rest_framework.response import Response

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    @detail_route(methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk = None):
        event = get_object_or_404(Event.objects.all(), pk = pk)
        event.likes += 1
        event.save()
        return Response(event.likes)


    # POST http://127.0.0.1:8000/events/
    def create(self, request, *args, **kwargs):
        serialized = EventSerializer(data=request.data)
        organizer= Organizer.objects.get(id=serialized.initial_data["organizer"],)
        event = Event(
                name=serialized.initial_data["name"],
                start_time=serialized.initial_data["start_time"],
                end_time=serialized.initial_data["end_time"],
                description=serialized.initial_data["description"],
                organizer = organizer,
                likes=serialized.initial_data["likes"],
                img_url=serialized.initial_data["img_url"],
            )
        event.save()
        return Response()#serialized.data, content_type="application/json")

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
#     "location": "TCT LT",
#     "description": "Gain first-hand understanding of what it's like to work in UBS.",
#     "organizer": 3,
#     "likes": 10,
#     "img_url": "http://goo.gl/TPdCQE"
# }