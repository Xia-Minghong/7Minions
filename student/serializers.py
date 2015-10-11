from rest_framework import serializers

from .models import Student, Friendship
from EMS.serializers import *
from .views import *


# class FriendshipSerializer(serializers.HyperlinkedModelSerializer):
#
#     id = serializers.Field(source='to_student.id')
#     name = serializers.Field(source='to_student.name')
#
#     class Meta:
#         model = Friendship
#         fields = ('id', 'name', )


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        user = UserSerializer
        # friends = FriendshipSerializer(source='friendship_set', many=True)
        #friends = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        # url is optional
        fields = ('user', 'department', 'name', 'matric_no', 'img_url', )
        depth = 1


