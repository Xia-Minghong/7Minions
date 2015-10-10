from django.db import models
from event.models import Event

# Create your models here.

class Feedback(models.Model):
    event = models.ForeignKey(Event, default=1)
    content = models.CharField(max_length = 200)
    rating = models.IntegerField()

    def __str__(self):
        return str(self.event) + ' : ' + self.content