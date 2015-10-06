# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tag', models.CharField(max_length=40)),
                ('event', models.ForeignKey(to='event.Event')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('tag', 'event')]),
        ),
    ]
