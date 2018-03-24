# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-24 09:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingentry',
            name='month',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 24, 9, 9, 30, 957607)),
        ),
        migrations.AlterField(
            model_name='connection',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 24, 9, 9, 30, 954456)),
        ),
        migrations.AlterField(
            model_name='loginentry',
            name='auth_token',
            field=models.CharField(default=b'a8edc735-6f8d-4fe0-951d-2ee69aedab3b', max_length=512),
        ),
        migrations.AlterField(
            model_name='loginentry',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 24, 9, 9, 30, 955735)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 24, 9, 9, 30, 957092)),
        ),
    ]
