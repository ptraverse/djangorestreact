# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-21 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=512)),
                ('primary_color', models.CharField(max_length=6)),
                ('secondary_color', models.CharField(max_length=6)),
            ],
        ),
    ]
