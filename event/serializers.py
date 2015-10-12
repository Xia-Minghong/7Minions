from rest_framework import serializers

from .models import Event, registered_or_attended
from organizer.serializers import OrganizerSerializer

class EventSerializer(serializers.ModelSerializer):

    organizer = OrganizerSerializer
    class Meta:
        model = Event
        fields = ('id', 'name', 'start_time', 'end_time', 'location', 'description', 'likes', 'img_url', 'organizer', 'tag_set')
        depth = 1

def serialize_event_for_student(event, student, many):
    if many:
        list=[]
        for e in event:
            registered, attended=registered_or_attended(event=e, student=student)
            data=EventSerializer(e).data
            data['registered']=registered
            data['attended']=attended
            list.append(data)
        return list
    else:
        registered, attended=registered_or_attended(event=event, student=student)
        data=EventSerializer(event).data
        data['registered']=registered
        data['attended']=attended
        return data