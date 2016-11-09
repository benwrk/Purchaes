# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-09 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.TextField(default='', max_length=50)),
                ('bio', models.TextField(max_length=1000)),
            ],
        ),
    ]
