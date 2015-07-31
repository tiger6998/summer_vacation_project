# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('release_date', models.DateField()),
                ('runtime', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('Genre', models.CharField(max_length=100)),
                ('storyline', models.TextField()),
                ('picture', models.ImageField(upload_to=b'media', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('career', models.CharField(max_length=1, choices=[('A', 'Actor'), ('W', 'Writer'), ('L', 'Director')])),
                ('intro', models.TextField()),
                ('born', models.DateField()),
                ('photo', models.ImageField(upload_to=b'media', blank=True)),
            ],
        ),
    ]
