# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0002_auto_20171221_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackersystem',
            name='Daily_Hydrate_Volume',
            field=models.FloatField(null=True),
        ),
    ]
