# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-27 22:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0041_auto_20180327_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 22, 7, 22, 57642)),
        ),
        migrations.AlterField(
            model_name='loginentry',
            name='auth_token',
            field=models.CharField(default=b'26575b80-cde5-4060-9e1a-abab79320fbc', max_length=512),
        ),
        migrations.AlterField(
            model_name='loginentry',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 22, 7, 22, 60672)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 22, 7, 22, 62999)),
        ),
    ]