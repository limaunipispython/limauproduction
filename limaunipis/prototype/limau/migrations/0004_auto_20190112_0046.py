# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-11 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limau', '0003_auto_20190112_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='type a description of your recipe, use html tag if necessary'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredient_content',
            field=models.TextField(default='type your ingredients here, use html tag if necessary'),
        ),
        migrations.AlterField(
            model_name='userrecipe',
            name='ingredients',
            field=models.TextField(default='key in your ingredients here in numbers form, eg, 1.Gula '),
        ),
        migrations.AlterField(
            model_name='userrecipe',
            name='instructions',
            field=models.TextField(default='key in your ingredients here in numbers form, eg 1.Masukkan Gula dan Garam'),
        ),
    ]
