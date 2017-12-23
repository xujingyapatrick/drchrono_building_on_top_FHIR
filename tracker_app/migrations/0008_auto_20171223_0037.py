# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0007_auto_20171223_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
