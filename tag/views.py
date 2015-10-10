from django.shortcuts import render


from rest_framework.decorators import list_route, detail_route
from rest_framework import viewsets, permissions
from .models import Tag, tags
from .serializers import TagSerializer
from rest_framework.response import Response
# Create your views here.
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # provided: [GET].list(), [GET].retrieve(), [POST].create(), [PUT].update(), and [DELETE].destroy()

    # http://127.0.0.1:8000/tags/career/get_events
    @detail_route(methods=['get'])
    def get_events(self, request, **kwargs):
        event_list = Tag.objects.filter(tag = kwargs['pk'])
        serializer = TagSerializer(event_list,many=True)

        return Response(serializer.data, content_type="application/json")
