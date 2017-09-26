# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 04:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import ekart.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to=ekart.models.get_image_path)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekart.Artist')),
            ],
        ),
    ]