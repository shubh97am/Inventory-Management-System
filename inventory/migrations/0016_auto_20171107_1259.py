# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_businessprofile_c_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]