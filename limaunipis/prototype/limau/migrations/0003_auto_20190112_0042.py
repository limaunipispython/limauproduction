# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-11 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limau', '0002_restaurant_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrecipe',
            name='ingredients',
            field=models.TextField(default='key in your ingredients here in numbers form, use html tag if necessary'),
        ),
        migrations.AlterField(
            model_name='userrecipe',
            name='instructions',
            field=models.TextField(default='key in your ingredients here in numbers form, use html tag if necessary'),
        ),
    ]
