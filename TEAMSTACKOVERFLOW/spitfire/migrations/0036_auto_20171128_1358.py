# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spitfire', '0035_auto_20171128_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackcomment',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='trackcomment',
            name='text',
        ),
        migrations.RemoveField(
            model_name='trackcomment',
            name='track',
        ),
        migrations.RemoveField(
            model_name='trackcomment',
            name='upvotes',
        ),
        migrations.AlterField(
            model_name='trackcomment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]