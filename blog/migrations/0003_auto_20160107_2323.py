# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 06:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=datetime.datetime(2016, 1, 8, 6, 23, 56, 264419, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
