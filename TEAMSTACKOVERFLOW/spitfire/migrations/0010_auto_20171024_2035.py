# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spitfire', '0009_auto_20171024_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='propic',
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
