# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20171106_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='c_timezone',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
