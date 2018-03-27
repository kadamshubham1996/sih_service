# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-27 04:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0021_auto_20180327_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 4, 14, 27, 901799)),
        ),
        migrations.AlterField(
            model_name='loginentry',
            name='auth_token',
            field=models.CharField(default=b'1400930c-7b4e-4ee5-b788-dee07d842964', max_length=512),
        ),
        migrations.AlterField(
            model_name='loginentry',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 4, 14, 27, 903356)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 4, 14, 27, 904575)),
        ),
    ]