# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-07 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import evaluation.models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0004_auto_20170905_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=evaluation.models.upload_location, verbose_name='Atach a File'),
        ),
        migrations.AlterField(
            model_name='question',
            name='evaluation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='evaluation.Evaluation'),
        ),
    ]