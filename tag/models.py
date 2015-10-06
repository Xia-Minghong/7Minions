from django.db import models
from event.models import Event
# Create your models here.


class Tag(models.Model):

    event = models.ForeignKey(Event)
    tag = models.CharField(max_length=40)

    def __str__(self):
        return self.event + ' : ' + self.tag

    class Meta:
        unique_together = (("event", "tag"),)