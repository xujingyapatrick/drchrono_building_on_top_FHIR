# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0004_trackersystem_daily_sleep_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.CharField(max_length=140, serialize=False, primary_key=True)),
            ],
        ),
    ]
