# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-19 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_auto_20181219_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featureproduct',
            field=models.BooleanField(choices=[(True, '是'), (False, '否')], default=True, verbose_name='特色产品'),
        ),
    ]
