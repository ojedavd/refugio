# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-05-14 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=70)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('domicilio', models.TextField()),
            ],
        ),
    ]
