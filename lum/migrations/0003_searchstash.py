# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-19 02:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lum', '0002_auto_20160714_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchStash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_used', models.CharField(max_length=255, verbose_name=b'Search Used')),
                ('pmids', models.ManyToManyField(to='lum.Publication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
