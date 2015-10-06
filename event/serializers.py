from rest_framework import serializers

from .models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'name', 'start_time', 'end_time', 'location', 'description', 'organizer', 'likes', 'img_url')

