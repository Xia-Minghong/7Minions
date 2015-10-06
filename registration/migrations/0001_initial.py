# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('event', models.ForeignKey(to='event.Event', related_name='event')),
                ('student', models.ForeignKey(to='student.Student', related_name='student')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together=set([('student', 'event')]),
        ),
    ]
