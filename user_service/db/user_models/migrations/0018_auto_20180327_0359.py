# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-27 03:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0017_auto_20180327_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 3, 59, 9, 735184)),
        ),
        migrations.AlterField(
            model_name='loginentry',
            name='auth_token',
            field=models.CharField(default=b'1015e688-c894-4ab2-ba64-f6d092791604', max_length=512),
        ),
        migrations.AlterField(
            model_name='loginentry',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 3, 59, 9, 736700)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 3, 59, 9, 738033)),
        ),
    ]
