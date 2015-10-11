from rest_framework import serializers

from .models import Event
from organizer.serializers import OrganizerSerializer

class EventSerializer(serializers.ModelSerializer):

    # def __init__(self, student=None):
    #

    organizer = OrganizerSerializer
    class Meta:
        model = Event
        fields = ('id', 'name', 'start_time', 'end_time', 'location', 'description', 'likes', 'img_url', 'organizer', 'tag_set')
        depth = 1
