# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spitfire', '0012_auto_20171025_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='keywords',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
