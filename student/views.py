from django.shortcuts import render
from student.models import *
from .serializers import *
import json

from rest_framework.decorators import list_route, detail_route
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # provided: [GET].list(), [GET].retrieve(), [POST].create(), [PUT].update(), and [DELETE].destroy()


    # http://127.0.0.1:8000/student/2/some_action/
    @detail_route(methods=['post'])
    def some_action(self, request, pk=None):

        return Response(pk)

    # # http://127.0.0.1:8000/student/2/update/
    # @detail_route(methods=['put'])
    # def update(self, request, pk):
    #     return Response(pk)

    # http://127.0.0.1:8000/student/another/
    @list_route(methods=['get'])    # can be post as well
    def another(self, request):
        return Response("1")

    # # http://127.0.0.1:8000/student/signup/
    # @list_route(methods=['post'])    # can be post as well
    # def signup(self, request):
    #     StudentSerializer
    #     return Response(request.data["name"])
# serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
