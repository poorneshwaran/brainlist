# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-19 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brainstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brainno', models.CharField(max_length=30)),
                ('seriesid', models.CharField(max_length=30)),
                ('dateofperf', models.DateTimeField()),
                ('dateofimg', models.DateTimeField()),
                ('status', models.IntegerField()),
                ('lastupdate', models.DateTimeField()),
                ('nextstep', models.IntegerField()),
            ],
        ),
    ]