# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-26 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=500)),
                ('time', models.TimeField(default=3000)),
                ('category', models.CharField(default='none', max_length=100)),
                ('price_min', models.IntegerField(default=0)),
                ('price_max', models.IntegerField(default=10000000)),
                ('creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='tag',
            field=models.ManyToManyField(to='items.Tag'),
        ),
    ]