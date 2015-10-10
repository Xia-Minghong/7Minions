from rest_framework import serializers
from tag.serializers import TagSerializer
from .models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'name', 'start_time', 'end_time', 'location', 'description', 'likes', 'img_url', 'organizer')#, 'tag_set')
        depth = 1
