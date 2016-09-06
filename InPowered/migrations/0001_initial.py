# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParsedPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(blank=True, max_length=50)),
                ('page_description', models.CharField(blank=True, max_length=50)),
                ('page_summary', models.CharField(blank=True, max_length=50)),
                ('page_author', models.CharField(blank=True, max_length=50)),
                ('page_date', models.CharField(blank=True, max_length=50)),
                ('page_polarity', models.CharField(blank=True, max_length=50)),
                ('page_subjectivity', models.CharField(blank=True, max_length=50)),
                ('page_related_confidence_numbers', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
