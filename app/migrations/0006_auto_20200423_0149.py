# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-22 22:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200423_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 4, 23, 1, 49, 43, 384183), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 4, 23, 1, 49, 43, 386177), verbose_name='Дата'),
        ),
    ]