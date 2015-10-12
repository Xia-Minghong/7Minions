from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Event
from .serializers import EventSerializer, serialize_event_for_student
from rest_framework.decorators import list_route, detail_route
from organizer.models import Organizer
from rest_framework.response import Response

from rest_framework.decorators import detail_route
from rest_framework.response import Response


def get_registered_participants(event):
    from student.models import Registration
    registrations = Registration.objects.filter(event=event)
    participants = []
    for registration in registrations:
        participants.append(registration.student)
    from student.serializers import StudentSerializer
    data = StudentSerializer(participants, many=True).data
    return data


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('start_time')
    serializer_class = EventSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset_list = list(queryset)
        #user = request.user.student
        #preference = ('community',  'concert', 'career')
        preference = ('career', )
        resultset = []
        for event in queryset_list:
            cur_match = 0
            for event_tags in event.tag_set.values_list():
                for pref in preference:
                    if pref in event_tags:
                        cur_match += 1
            index = 0
            for result in resultset:
                pre_match = 0
                for result_tags in result.tag_set.values_list():
                    for pref in preference:
                        if pref in result_tags:
                            pre_match += 1
                if cur_match > pre_match:
                    resultset.insert(index, event)
                    break;
                index += 1
            if index == len(resultset):
                resultset.append(event)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        #serializer = self.get_serializer(resultset, many=True)
        #return Response(serializer.data)
        data = serialize_event_for_student(resultset, request.user.student, many=True)
        return Response(data)

    # GET http://127.0.0.1:8000/events/list_all/
    @list_route(methods=['get'])
    def list_all(self, request, *args, **kwargs):
        student = request.user.student
        events = Event.objects.all().order_by('start_time')
        data = serialize_event_for_student(student=student, event=events, many=True)
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        student = request.user.student
        event = Event.objects.get(id=kwargs['pk'])
        data = serialize_event_for_student(student=student, event=event)
        registered_participants = get_registered_participants(event)
        data["registered_participants"]=registered_participants
        return Response(data, content_type="application/json")

    # Like an event
    # GET  http://127.0.0.1:8000/events/12/like
    @detail_route(methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk = None):
        event = get_object_or_404(Event.objects.all(), pk = pk)
        event.likes += 1
        event.save()
        return Response(event.likes)

    # Create an event
    # POST http://127.0.0.1:8000/events/
    # {
    # "name": "UBS Career Talk",
    # "start_time": "2015-10-31T10:00:00Z",
    # "end_time": "2015-10-31T13:00:00Z",
    # "location": "TCT LT",
    # "description": "Gain first-hand understanding of what it's like to work in UBS.",
    # "likes": 10,
    # "img_url": "http://goo.gl/TPdCQE",
    # "organizer": 3
    # }

    def create(self, request, *args, **kwargs):
        serialized = EventSerializer(data=request.data)
        if(serialized.is_valid()):
            organizer= Organizer.objects.get(id=serialized.initial_data["organizer"],)
            event = Event(
                    name=serialized.initial_data["name"],
                    start_time=serialized.initial_data["start_time"],
                    end_time=serialized.initial_data["end_time"],
                    location = serialized.initial_data["location"],
                    description=serialized.initial_data["description"],
                    organizer = organizer,
                    likes=serialized.initial_data["likes"],
                    img_url=serialized.initial_data["img_url"],
                )
            event.save()
            return Response(request.data, content_type="application/json")
        else:
            return Response(serialized._errors)

# View all events
# GET  http://127.0.0.1:8000/events/

# View an event
# GET  http://127.0.0.1:8000/events/1/



