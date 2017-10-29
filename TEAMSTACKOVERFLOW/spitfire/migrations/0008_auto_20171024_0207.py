# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spitfire', '0007_auto_20171023_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lyriccomment',
            name='lyrics',
        ),
        migrations.RemoveField(
            model_name='lyrics',
            name='track',
        ),
        migrations.AddField(
            model_name='lyrics',
            name='LyricComment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spitfire.LyricComment'),
        ),
        migrations.AddField(
            model_name='lyrics',
            name='Track',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spitfire.Track'),
        ),
    ]