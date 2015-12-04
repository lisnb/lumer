# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan_set',
            field=models.CharField(max_length=1, choices=[(1, '\u5957\u99101'), (2, '\u5957\u99102'), (3, '\u5957\u99103'), (4, '\u5957\u99104'), (5, '\u5957\u99105'), (6, '\u5957\u99106'), (7, '\u5957\u99107')]),
        ),
    ]
