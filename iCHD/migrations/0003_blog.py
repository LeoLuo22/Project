# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-08 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iCHD', '0002_auto_20160907_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
