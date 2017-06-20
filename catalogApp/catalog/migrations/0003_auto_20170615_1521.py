# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20170613_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media_type',
            field=models.CharField(choices=[('F', 'Film'), ('B', 'Book'), ('A', 'Album')], max_length=50),
        ),
    ]
