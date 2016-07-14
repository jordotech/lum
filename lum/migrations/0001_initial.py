# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-14 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name=b'Name')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Name')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Address')),
                ('organization', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Organization')),
                ('department', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'Department')),
                ('city', models.CharField(blank=True, max_length=150, null=True, verbose_name=b'City')),
                ('province', models.CharField(blank=True, max_length=100, verbose_name=b'Province')),
                ('postal_code', models.CharField(blank=True, max_length=11, null=True, verbose_name=b'Postal Code')),
                ('country', models.CharField(blank=True, max_length=30, null=True, verbose_name=b'Country')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name=b'Phone')),
            ],
            options={
                'verbose_name': 'Lab',
                'verbose_name_plural': 'Labs',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.CharField(max_length=255, verbose_name=b'PMID')),
                ('abstract', models.TextField(blank=True, null=True, verbose_name=b'Abstract')),
                ('doi', models.CharField(blank=True, help_text=b'Digital object identifier', max_length=255, null=True, verbose_name=b'DOI')),
                ('authors', models.ManyToManyField(related_name='author_set', to='lum.Author', verbose_name=b'authors')),
                ('labs', models.ManyToManyField(blank=True, related_name='pub_set', to='lum.Lab', verbose_name=b'labs')),
            ],
            options={
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publications',
            },
        ),
        migrations.AddField(
            model_name='author',
            name='labs',
            field=models.ManyToManyField(blank=True, related_name='author_set', to='lum.Lab', verbose_name=b'labs'),
        ),
    ]
