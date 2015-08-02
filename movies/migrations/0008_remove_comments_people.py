# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='people',
        ),
    ]
