from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student
        # url is optional
        fields = ('url', 'department', 'name', 'matric_no', 'email')