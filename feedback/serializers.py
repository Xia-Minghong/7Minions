from rest_framework import serializers

from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ('event', 'content', 'rating')
        depth = 1
        # list_seriali