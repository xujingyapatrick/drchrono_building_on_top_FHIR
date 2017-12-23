# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trackersystem',
            old_name='patient_dbp',
            new_name='Daily_Diastolic_Blood_Pressure',
        ),
        migrations.RenameField(
            model_name='trackersystem',
            old_name='patient_sbp',
            new_name='Daily_Systolic_Blood_Pressure',
        ),
        migrations.RenameField(
            model_name='trackersystem',
            old_name='patient_weight',
            new_name='Daily_Weight',
        ),
        migrations.RenameField(
            model_name='trackersystem',
            old_name='date',
            new_name='Date',
        ),
    ]
