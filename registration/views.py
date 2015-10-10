from django.shortcuts import render


from rest_framework.decorators import list_route, detail_route
from rest_framework import viewsets, permissions
from .models import Registration
from .models import Event
from .serializers import RegistrationSerializer
from rest_framework.response import Response
# Create your views here.
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    # provided: [GET].list(), [GET].retrieve(), [POST].create(), [PUT].update(), and [DELETE].destroy()

    # http://127.0.0.1:8000/registrations/1/register_event
    @detail_route(methods=['get'])
    def register_event(self, request, **kwargs):
        event = Event.objects.get(id = kwargs["pk"]).student
        serializer = StudentSerializer(student)
        return Response(serializer.data, content_type="application/json")
        User.objects.get(id = kwargs["pk"]).student
        serializer = RegistrationSerializer(event_list, many=True)
        return Response(serializer.data, content_type="application/json")
