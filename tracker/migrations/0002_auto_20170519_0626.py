# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-19 06:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='date',
            field=models.DateField(default=datetime.date(2017, 5, 19)),
        ),
        migrations.AlterField(
            model_name='planting',
            name='date',
            field=models.DateField(default=datetime.date(2017, 5, 19)),
        ),
    ]
