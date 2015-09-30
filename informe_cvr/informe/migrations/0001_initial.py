# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CVRSection',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.TextField()),
                ('body', django_markdown.models.MarkdownField()),
                ('body_html', models.TextField()),
                ('slug', models.SlugField(unique=True, max_length=125)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Sección del Informe CVR',
                'verbose_name_plural': 'Secciones del Informe CVR',
            },
        ),
    ]
