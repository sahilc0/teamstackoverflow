# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 18:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spitfire', '0032_auto_20171128_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='image',
        ),
        migrations.RemoveField(
            model_name='trackcomment',
            name='artist',
        ),
    ]