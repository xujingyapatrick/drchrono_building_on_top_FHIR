# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0005_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackersystem',
            name='patient',
            field=models.ForeignKey(default=datetime.datetime(2017, 12, 22, 11, 0, 12, 305663, tzinfo=utc), to='tracker_app.Patient'),
            preserve_default=False,
        ),
    ]
