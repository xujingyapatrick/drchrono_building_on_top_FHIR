# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0008_auto_20171223_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
        ),
    ]
