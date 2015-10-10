from django.db import models
from organizer.models import Organizer
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    organizer = models.ForeignKey(Organizer)
    likes = models.IntegerField()
    img_url = models.CharField(max_length=200, default="", null=True)

    def __str__(self):
       return self.name + ' : ' + self.location