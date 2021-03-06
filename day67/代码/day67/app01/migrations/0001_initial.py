# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-06-03 02:24
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
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('gender', models.IntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'others')], verbose_name='性别')),
            ],
        ),
    ]
