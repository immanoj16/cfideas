# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20170320_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='page',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
