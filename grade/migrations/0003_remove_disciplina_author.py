# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 16:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0002_auto_20170928_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='author',
        ),

    ]
