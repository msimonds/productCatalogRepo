# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_genre_extra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='extra',
        ),
    ]
