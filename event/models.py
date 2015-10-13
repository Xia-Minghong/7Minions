from django.db import models
from organizer.models import Organizer

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    organizer = models.ForeignKey(Organizer, default=1)
    likes = models.IntegerField(default=0)
    img_url = models.CharField(max_length=200, default="http://s3.amazonaws.com/gametizeblog/images/2014/07/events-heavenly-header1.jpg", null=True)

    def participant_list_field(self):
        from .views import registered_participants
        return registered_participants(self)

    def __str__(self):
       return self.name + ' : ' + self.location


def registered_or_attended(event, student):
    from student.models import Registration

    #object does not exist when get() is called
    registrations = Registration.objects.filter(student=student, event=event)
    if registrations:
        return (True, registrations[0].attended)
    else:
        return (False,False)