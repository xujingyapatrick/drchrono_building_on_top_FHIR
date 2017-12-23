# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0003_trackersystem_daily_hydrate_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackersystem',
            name='Daily_Sleep_Time',
            field=models.FloatField(null=True),
        ),
    ]
