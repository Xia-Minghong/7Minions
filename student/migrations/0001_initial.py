# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('department', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('matric_no', models.CharField(unique=True, max_length=9)),
                ('email', models.EmailField(unique=True, max_length=100)),
                ('friends', models.ManyToManyField(to='student.Student', through='student.Friendship', related_name='related_to+')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='friendship',
            name='from_student',
            field=models.ForeignKey(to='student.Student', related_name='from_student'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='to_student',
            field=models.ForeignKey(to='student.Student', related_name='to_student'),
        ),
    ]
