from django.db import models
from event.models import Event
# Create your models here.

class Registration(models.Model):

    tag = models.CharField(max_length=40)
    event = models.ForeignKey(Event)

    class Meta:
        unique_together = (("student", "event"),)