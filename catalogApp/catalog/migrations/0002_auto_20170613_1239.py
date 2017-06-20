# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='Untitled', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='media_type',
            field=models.CharField(choices=[('B', 'Book'), ('F', 'Film'), ('A', 'Album')], max_length=50),
        ),
    ]
