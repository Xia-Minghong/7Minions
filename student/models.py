from django.db import models

# Create your models here.
class Student(models.Model):
    matric_no = models.CharField(max_length=9)
    name = models.CharField(max_length=40)
    friends = models.ManyToManyField('self', through='Friendship',
                                           symmetrical=False,
                                           related_name='related_to')

    # def __unicode__(self):
    #    return 'Student: ' + self.name

class Friendship(models.Model):
    from_student = models.ForeignKey(Student, related_name='from_student')
    to_student = models.ForeignKey(Student, related_name='to_student')
    # status = models.IntegerField(choices=RELATIONSHIP_STATUSES)

