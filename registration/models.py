from django.db import models
from event.models import Event
from student.models import Student
# Create your models here.

class Registration(models.Model):

    student = models.ForeignKey(Student, related_name="student")
    event = models.ForeignKey(Event, related_name="event")

    class Meta:
        unique_together = (("student", "event"),)