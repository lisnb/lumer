# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_set', models.CharField(max_length=1, choices=[(1, b'\xe5\xa5\x97\xe9\xa4\x901'), (2, b'\xe5\xa5\x97\xe9\xa4\x902'), (3, b'\xe5\xa5\x97\xe9\xa4\x903'), (4, b'\xe5\xa5\x97\xe9\xa4\x904'), (5, b'\xe5\xa5\x97\xe9\xa4\x905'), (6, b'\xe5\xa5\x97\xe9\xa4\x906'), (7, b'\xe5\xa5\x97\xe9\xa4\x907')])),
                ('name', models.CharField(max_length=60)),
                ('duration', models.DurationField(default=datetime.timedelta(28))),
                ('weekdays', models.CharField(max_length=100)),
            ],
        ),
    ]
