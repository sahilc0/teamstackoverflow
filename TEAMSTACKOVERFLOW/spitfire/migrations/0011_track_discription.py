# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spitfire', '0010_auto_20171024_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='discription',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
