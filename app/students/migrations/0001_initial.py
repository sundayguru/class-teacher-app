# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-05 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=140)),
                ('last_name', models.CharField(max_length=140)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='classes.Classes')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]