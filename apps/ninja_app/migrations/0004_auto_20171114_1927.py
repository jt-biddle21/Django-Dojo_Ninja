# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-14 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninja_app', '0003_auto_20171114_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default=0),
        ),
    ]