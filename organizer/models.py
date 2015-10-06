from django.db import models

# Create your models here.

class Organizer(models.Model):
    name = models.CharField(max_length=20,unique=True)
    description = models.CharField(max_length=200)
    img_url = models.CharField(max_length=100, null=True, default="")

    def __str__(self):
       return self.name + ' : ' + self.description