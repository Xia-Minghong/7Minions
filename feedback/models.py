from django.db import models

# Create your models here.

class Feedback(models.Model):
    content = models.CharField(max_length=200)
    rating = models.IntegerField()
