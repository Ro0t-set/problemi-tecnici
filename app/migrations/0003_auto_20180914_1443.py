# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-14 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_problema_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problema',
            name='descrizioneProblema',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
