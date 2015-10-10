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

    @detail_route(methods=['get'])
    def getevents(self, request, **kwargs):
        # event_list = Tag.objects.get(tag = 'career')#filter(tag = kwargs['pk'])
        # pserializer = TagSerializer(event_list)
        event_list = Tag.objects.all()
        s = str(event_list)

        return Response(str(type(s)))#serializer.data, content_type="application/json")
