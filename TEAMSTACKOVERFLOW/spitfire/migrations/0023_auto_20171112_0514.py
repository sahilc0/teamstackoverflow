# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 10:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spitfire', '0022_auto_20171111_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='spitfire.User'),
        ),
    ]
