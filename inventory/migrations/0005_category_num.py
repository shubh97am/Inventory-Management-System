# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20171030_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='num',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
