# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_genre_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='extra',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
    ]
