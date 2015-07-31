# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='slug',
            field=models.SlugField(default=b''),
        ),
        migrations.AddField(
            model_name='people',
            name='slug',
            field=models.SlugField(default=b''),
        ),
    ]
