# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20170618_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(to='catalog.Genre', null=True, blank=True, related_name='children')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('media_type', models.CharField(max_length=50, choices=[('F', 'Film'), ('B', 'Book'), ('A', 'Album')])),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('parent', models.ForeignKey(to='catalog.Genre')),
            ],
        ),
    ]
