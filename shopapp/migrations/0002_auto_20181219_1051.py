# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-19 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200, verbose_name='产品描述'),
        ),
    ]
