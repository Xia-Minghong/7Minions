from django.shortcuts import render
from student.models import *
from .serializers import *
import json

from rest_framework.decorators import list_route, detail_route
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from EMS.serializers import *
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

    # http://127.0.0.1:8000/student/addfriend/
    @list_route(methods=['get'])    # can be post as well
    def addfriend(self, request):
        return Response("1")

    # def signup(request, matric_no, name):
    #     new_student = Student(matric_no=matric_no, name=name)
    #     new_student.save()
    #     return HttpResponse(json.dumps(serializers.serialize("json", [new_student])), content_type="application/json")
    #
    # def login(request):
    #     return HttpResponse(0)
