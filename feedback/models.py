from django.db import models
from event.models import Event

# Create your models here.

class Feedback(models.Model):
    # event = models.ForeignKey(Event)
    content = models.CharField(max_length = 200)
    rating = models.IntegerField()

    def __str__(self):
        return "abc"#str(self.event) + ' : ' + self.content