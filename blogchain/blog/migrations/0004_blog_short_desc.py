# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-03-19 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230314_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_desc',
            field=models.CharField(default='', max_length=250),
        ),
    ]