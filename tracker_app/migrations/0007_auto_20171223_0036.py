# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0006_trackersystem_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='birthDate',
            field=models.CharField(default=datetime.datetime(2017, 12, 23, 0, 36, 31, 962367, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='contacts',
            field=models.CharField(default=datetime.datetime(2017, 12, 23, 0, 36, 38, 21455, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default=datetime.datetime(2017, 12, 23, 0, 36, 44, 848097, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(default=datetime.datetime(2017, 12, 23, 0, 36, 50, 317515, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.IntegerField(max_length=140, serialize=False, primary_key=True),
        ),
    ]
