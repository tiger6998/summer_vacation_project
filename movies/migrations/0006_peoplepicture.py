# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_moviepicture'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeoplePicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'media', blank=True)),
                ('people', models.ForeignKey(to='movies.People')),
            ],
        ),
    ]
