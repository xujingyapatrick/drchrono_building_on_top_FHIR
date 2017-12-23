# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trackerSystem',
            fields=[
                ('patient_sbp', models.FloatField(null=True)),
                ('patient_dbp', models.FloatField(null=True)),
                ('patient_weight', models.FloatField(null=True)),
                ('date', models.DateTimeField(serialize=False, primary_key=True)),
            ],
        ),
    ]
