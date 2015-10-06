# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.AlterField(
            model_name='friendship',
            name='from_student',
            field=models.ForeignKey(to='student.Student', related_name='from_students'),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='to_student',
            field=models.ForeignKey(to='student.Student', related_name='to_students'),
        ),
    ]
