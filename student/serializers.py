from rest_framework import serializers

from .models import Student
from ems.serializers import *

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        user = UserSerializer
        # url is optional
        fields = ('user', 'department', 'name', 'matric_no')