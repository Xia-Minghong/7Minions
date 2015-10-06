# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20150929_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='img_url',
            field=models.CharField(max_length=100, null=True, default=''),
        ),
    ]
