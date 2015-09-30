from rest_framework import serializers
from django.contrib.auth.models import User, Group


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group