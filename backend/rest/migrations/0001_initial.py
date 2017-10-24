# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 11:56
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
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-username',),
            },
        ),
    ]