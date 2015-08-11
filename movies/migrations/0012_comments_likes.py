# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
