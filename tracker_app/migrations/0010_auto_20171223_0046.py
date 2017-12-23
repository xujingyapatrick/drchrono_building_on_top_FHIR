# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0009_auto_20171223_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='birthDate',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='name',
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
