from django.db import models
from django.contrib.auth.models import User
from event.models import Event

# Create your models here.
class Student(models.Model):

    user = models.OneToOneField(User)

    department = models.CharField(max_length=100)

    name = models.CharField(max_length=50)

    matric_no = models.CharField(max_length=9, unique=True)

    img_url = models.CharField(max_length=200, null=True, default="")

    #preference = models.

    friends = models.ManyToManyField('self', through='Friendship', symmetrical=False,
                                           related_name='related_to+'
                                           )
    registrations = models.ManyToManyField('self', through='Registration', symmetrical=False, related_name='registered+')

    bookmarks = models.ManyToManyField('self', through='Bookmark', symmetrical=False, related_name='bookmarked+')

    def __str__(self):
       return self.name + ' : ' + self.matric_no

    def signup(self, request):
        Student.objects.get_or_create(department=request.data["department"], name="name")

    def add_friendship(self, friend, symm=True):
        friendship, created = Friendship.objects.get_or_create(
            from_student= self,
            to_student= friend)
        if symm:
            # avoid recursion by passing `symm=False`
            friend.add_friendship(self, False)
        return friendship

    def remove_friendship(self, person, symm=True):
        Friendship.objects.filter(
            from_student=self,
            to_student=person).delete()
        if symm:
            # avoid recursion by passing `symm=False`
            person.remove_friendship(self, False)

    def get_friendships(self, status):
        return self.friendships.filter(
            to_students__from_student=self)


class Friendship(models.Model):
    from_student = models.ForeignKey(Student, related_name='from_students')
    to_student = models.ForeignKey(Student, related_name='to_students')

    class Mata:
        unique_together = ('from_student', 'to_student')

class Registration(models.Model):
    student = models.ForeignKey(Student, related_name='student_registration')
    event = models.ForeignKey(Event, related_name='event_registration')
    attended = models.BooleanField(default=False)

    class Mata:
        unique_together = ('student', 'event')


class Bookmark(models.Model):
    student = models.ForeignKey(Student, related_name='student_bookmark')
    event = models.ForeignKey(Event, related_name='event_bookmark')

    class Mata:
        unique_together = ('student', 'event')


