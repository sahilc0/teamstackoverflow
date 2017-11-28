# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('spitfire', '0036_auto_20171128_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackcomment',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spitfire.Artist'),
        ),
        migrations.AddField(
            model_name='trackcomment',
            name='text',
            field=models.TextField(default='blah', help_text='Enter a comment', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trackcomment',
            name='track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spitfire.Track'),
        ),
        migrations.AddField(
            model_name='trackcomment',
            name='upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trackcomment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular lyrics across whole site', primary_key=True, serialize=False),
        ),
    ]
