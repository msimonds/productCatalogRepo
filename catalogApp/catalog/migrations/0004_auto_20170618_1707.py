# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20170615_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='product',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
