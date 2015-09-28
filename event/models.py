from django.db import models
from organizer.models import Organizer
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    #tag =
    organizer = models.ForeignKey(Organizer)
    likes = models.IntegerField()