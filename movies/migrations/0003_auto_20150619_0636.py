# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20150619_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
