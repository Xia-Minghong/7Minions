from django.shortcuts import render
from student.models import *
from .serializers import *
import json
from rest_framework.renderers import JSONRenderer

from rest_framework.decorators import list_route, detail_route
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from EMS.serializers import *
from .serializers import StudentSerializer
from event.serializers import EventSerializer
from .models import Student

def get_bookmarked_events(student):
        bookmarks = Bookmark.objects.order_by('event__start_time').filter(student=student)
        events = []
        for bookmark in bookmarks:
            events.append(bookmark.event)
        data = EventSerializer(events, many=True).data
        return data

def get_registered_events(student):
        registrations = Registration.objects.order_by('event__start_time').filter(student=student)
        events = []
        for registration in registrations:
            events.append(registration.event)
        data = EventSerializer(events, many=True).data
        return data

def get_friends(student):
        friendships = Friendship.objects.filter(to_student=student)
        friends = []
        for friendship in friendships:
            friends.append(friendship.to_student)
        data = StudentSerializer(friends, many=True).data
        return data

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # provided: [GET].list(), [GET].retrieve(), [POST].create(), [PUT].update(), and [DELETE].destroy()

    # Registration (override .create())
    @list_route(methods=['post'], permission_classes=[permissions.AllowAny])
    def signup(self, request, *args, **kwargs):

        serialized = UserSerializer(data=request.data)
        if(serialized.is_valid()):
            user = User.objects.create_user(
                serialized.initial_data["username"],
                "",
                serialized.initial_data["password"],
            )

            student = Student(
                user=user,
                department=serialized.initial_data["department"],
                name=serialized.initial_data["name"],
                matric_no=serialized.initial_data["matric_no"],
            )
            student.save()
            student_serialized = StudentSerializer(instance=student)
            return Response(student_serialized.data)
        else:
            return Response(serialized._errors)


    # GET http://127.0.0.1:8000/students/me/
    @list_route(methods=['get'])
    def me(self, request):
        student = request.user.student
        serializer = StudentSerializer(student)
        data = serializer.data
        friends = get_friends(student)
        bookmarked_event_data = get_bookmarked_events(student)
        registered_event_data = get_registered_events(student)
        data["friends"]=friends
        data["bookmarked_events"]=bookmarked_event_data
        data["registered_events"]=registered_event_data
        return Response(data, content_type="application/json")

    # http://127.0.0.1:8000/students/3/addfriend/
    @detail_route(methods=['post'])    # can be post as well
    def addfriend(self, request, *args, **kwargs):
        friend = User.objects.get(id = kwargs["pk"])
        request.user.student.add_friendship(friend.student)
        return Response(friend.username)

    # http://127.0.0.1:8000/students/3/removefriend/
    @detail_route(methods=['post'])    # can be post as well
    def removefriend(self, request, *args, **kwargs):
        friend = User.objects.get(id = kwargs["pk"])
        request.user.student.remove_friendship(friend.student)
        return Response(friend.username)

    # http://127.0.0.1:8000/students/12/
    @detail_route(methods=['get'])    # can be post as well
    def retrieve(self, request, *args, **kwargs):
        student = User.objects.get(id = kwargs["pk"]).student
        serializer = StudentSerializer(student)
        return Response(serializer.data, content_type="application/json")

    # http://127.0.0.1:8000/students/3/register_event/
    @detail_route(methods=['post'])    # can be post as well
    def register_event(self, request, **kwargs):
        student = request.user.student
        event = Event.objects.get(id = kwargs["pk"])
        registration, registered = Registration.objects.get_or_create(
            event= event,
            student= student)
        serializer = EventSerializer(event)
        if registered:
            return Response(serializer.data)
        else:
            return Response(registered)

    # http://127.0.0.1:8000/students/3/attend_event/
    @detail_route(methods=['put'])
    def attend_event(self, request, **kwargs):
        student = request.user.student
        event = Event.objects.get(id = kwargs["pk"])
        registration = Registration.objects.filter(
            event= event,
            student= student)
        #registration.attended = True
        registration.update(attended=True)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    # http://127.0.0.1:8000/students/3/deregister_event/
    @detail_route(methods=['delete'])
    def deregister_event(self, request, **kwargs):
        student = request.user.student
        event = Event.objects.get(id = kwargs["pk"])
        deregistration= Registration.objects.get(
            event= event,
            student= student)
        deregistration.delete()
        serializer = EventSerializer(event)
        return Response(serializer.data)

    # http://127.0.0.1:8000/students/3/bookmark_event/
    @detail_route(methods=['post'])
    def bookmark_event(self, request, **kwargs):
        student = request.user.student
        event = Event.objects.get(id = kwargs["pk"])
        bookmark, bookmarked = Bookmark.objects.get_or_create(
            event= event,
            student= student)
        serializer = EventSerializer(event)
        if bookmarked:
            return Response(serializer.data)
        else:
            return Response(bookmarked)

    # http://127.0.0.1:8000/students/bookmarkmarked_events/
    @list_route(methods=['get'])
    def bookmarked_events(self, request, **kwargs):
        student = request.user.student
        bookmarks = Bookmark.objects.filter(student=student)
        events = []
        for bookmark in bookmarks:
            events.append(bookmark.event)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


    # http://127.0.0.1:8000/students/3/unbookmark_event/
    @detail_route(methods=['delete'])
    def unbookmark_event(self, request, **kwargs):
        student = request.user.student
        event = Event.objects.get(id = kwargs["pk"])
        unbookmark= Bookmark.objects.get(
            event= event,
            student= student)
        unbookmark.delete()
        serializer = EventSerializer(event)
        return Response(serializer.data)
