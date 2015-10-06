from rest_framework import serializers

from .models import Organizer

class OrganizerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organizer
        fields = ('id', 'name', 'description', 'img_url')

