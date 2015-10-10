from rest_framework import serializers

from .models import Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('tag', 'event')
        # list_serializer_class = TagListSerializer


#
# class TagListSerializer(serializers.ListSerializer):
#     def create(self, validated_data):
#         tags = [Tag(**item) for item in validated_data]
#         return Tag.objects.bulk_create(tags)