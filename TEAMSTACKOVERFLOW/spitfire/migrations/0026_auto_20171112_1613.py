# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 21:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spitfire', '0025_auto_20171112_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artists', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]