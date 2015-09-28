from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):

    user = models.OneToOneField(User)

    department = models.CharField(max_length=100)

    name = models.CharField(max_length=50)

    matric_no = models.CharField(max_length=9, unique=True)

    email = models.EmailField(max_length=100, unique=True)
    #preference = models.

    friends = models.ManyToManyField('self', through='Friendship', symmetrical=False,
                                           related_name='related_to+'
                                           )

    def __str__(self):
       return self.name + ' : ' + self.matric_no


class Friendship(models.Model):
    from_student = models.ForeignKey(Student, related_name='from_student')
    to_student = models.ForeignKey(Student, related_name='to_student')
    # status = models.IntegerField(choices=RELATIONSHIP_STATUSES)

