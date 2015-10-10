from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    @detail_route(methods=['put', 'get'], permission_classes=[permissions.IsAuthenticated])
    def likes(self, request, pk = None):
        event = get_object_or_404(Event.objects.all(), pk = pk)
        if request.method == 'PUT':
            event.likes += 1
            event.save()
        return Response(event.likes)