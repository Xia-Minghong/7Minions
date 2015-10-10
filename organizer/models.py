from django.db import models



class Organizer(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.CharField(max_length=500)
    img_url = models.CharField(max_length=200, null=True, default="")

    def __str__(self):
       return self.name + ' : ' + self.description