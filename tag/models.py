from django.db import models
from event.models import Event
# Create your models here.
from student.models import Student

tags = ['sports', 'community',  'concert', 'career']

class Tag(models.Model):

    event = models.ForeignKey(Event)
    #student = models.ForeignKey(Student, default = 12)
    tag = models.CharField(max_length=40)

    def __str__(self):
        return str(self.event) + ' : ' + self.tag

    class Meta:
        unique_together = (("event", "tag"),)
