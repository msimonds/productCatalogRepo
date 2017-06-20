# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('genre_name', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(related_name='children', to='catalog.Genre', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('media_type', models.CharField(max_length=200, choices=[('B', 'Book'), ('F', 'Film'), ('A', 'Album')])),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('parent', models.ForeignKey(to='catalog.Genre')),
            ],
        ),
    ]
