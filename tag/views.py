from django.shortcuts import render


from rest_framework.decorators import list_route, detail_route
from rest_framework import viewsets, permissions
from .models import Tag, tags, Event
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
        serializer = TagSerializer(event_list, many=True)
        return Response(serializer.data, content_type="application/json")


    def create(self, request, *args, **kwargs):
        serialized = TagSerializer(data=request.data)
        if(serialized.is_valid()):
            event= Event.objects.get(id=serialized.initial_data["event"])
            tag = Tag(
                    event = event,
                    tag=serialized.initial_data["tag"],

                )
            tag.save()
            return Response(request.data, content_type="application/json")
        else:
            return Response(serialized._errors)
