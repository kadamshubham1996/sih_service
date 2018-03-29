# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-29 06:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0016_auto_20180329_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 29, 6, 13, 7, 594134)),
        ),
        migrations.AlterField(
            model_name='loginentry',
            name='auth_token',
            field=models.CharField(default=b'3f0d8386-a25a-431b-bae1-b9e3dfba4778', max_length=512),
        ),
        migrations.AlterField(
            model_name='loginentry',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 29, 6, 13, 7, 595668)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 29, 6, 13, 7, 596920)),
        ),
    ]