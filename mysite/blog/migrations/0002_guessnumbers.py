# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-25 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuessNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('blog', models.CharField(default='[1, 2, 3, 4, 5, 6]', max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('num_lotto', models.IntegerField(default=5)),
                ('update_date', models.DateTimeField()),
            ],
        ),
    ]
