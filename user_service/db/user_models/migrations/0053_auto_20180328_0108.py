# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-28 01:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0052_auto_20180328_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 28, 1, 8, 17, 950693)),
        ),
        migrations.AlterField(
            model_name='loginentry',
            name='auth_token',
            field=models.CharField(default=b'95f3e557-5d8d-4923-8c8d-f3f3cf2aa36b', max_length=512),
        ),
        migrations.AlterField(
            model_name='loginentry',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 28, 1, 8, 17, 952315)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 28, 1, 8, 17, 953486)),
        ),
    ]