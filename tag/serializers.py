from rest_framework import serializers
from event.serializers import EventSerializer
from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    event = EventSerializer
    class Meta:
        model = Tag
        # fields = ('tag', 'event')
        depth = 1
