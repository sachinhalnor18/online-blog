# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-03-14 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230314_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(max_length=100),
        ),
    ]
