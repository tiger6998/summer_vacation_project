# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20150630_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoviePicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'media', blank=True)),
                ('movie', models.ForeignKey(to='movies.Movies')),
            ],
        ),
    ]
