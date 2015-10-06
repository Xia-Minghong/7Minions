# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('event', 'tag')]),
        ),
    ]
