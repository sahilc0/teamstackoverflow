# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spitfire', '0043_contest_reward'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='description',
            field=models.TextField(default='Terrific Artist', max_length=2000),
            preserve_default=False,
        ),
    ]