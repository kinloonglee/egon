# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-06-02 02:49
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
                ('username', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '其他')])),
            ],
        ),
    ]
