from django.db import models

# Create your models here.
class Student(models.Model):
    matric_no = models.Charfield(max_length=9)
    name = models.CharField(max_length=40)