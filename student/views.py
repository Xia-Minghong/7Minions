from django.shortcuts import render
from student.models import *
from .serializers import *
import json

from rest_framework.decorators import list_route, detail_route
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from EMS.serializers import *
from .serializers import StudentSerializer
from event.serializers import EventSerializer
from .models import Student

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


    # POST http://127.0.0.1:8000/student/3/some_action/
    @detail_route(methods=['post'])
    def some_action(self, request, pk=None):
        return Response(request.user.id)

    # POST http://127.0.0.1:8000/student/another/
    @list_route(methods=['post'], permission_classes=[permissions.AllowAny])    # anybody is alloed
    def another(self, request):
        return Response("1")

    # GET http://127.0.0.1:8000/students/me/
    @list_route(methods=['get'])    # anybody is alloed
    def me(self, request):
        student = request.user.student
        serializer = StudentSerializer(student)
        return Response(serializer.data, content_type="application/json")

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

    # http://127.0.0.1:8000/students/3/bookmark/
    @detail_route(methods=['post'])
    def bookmark(self, request, **kwargs):
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

    # # http://127.0.0.1:8000/students/bookmark/
    # @list_route(methods=['get'])
    # def bookmark(self, request, **kwargs):
    #     #student = request.user.student
    #     #serializer = EventSerializer(student.bookmarks.all(), many=True)
    #     return Response()#serializer.data)
    #
    # # http://127.0.0.1:8000/students/3/bookmark/
    # @detail_route(methods=['delete'])
    # def bookmark(self, request, **kwargs):
    #     student = request.user.student
    #     event = Event.objects.get(id = kwargs["pk"])
    #     student.bookmarks.remove(event)
    #     serializer = EventSerializer(event)
    #     return Response(serializer.data)
