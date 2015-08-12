# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_comments_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='CastandCrew',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=1, choices=[('D', 'Director'), ('C', 'Cast'), ('W', 'Writer')])),
                ('celebs', models.ForeignKey(to='movies.People')),
                ('movie', models.ForeignKey(to='movies.Movies')),
            ],
        ),
    ]
