# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateField(default=b'2015-7-20'),
        ),
    ]
