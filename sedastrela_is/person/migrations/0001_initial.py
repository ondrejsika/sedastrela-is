# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('nick_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16)),
                ('mother_name', models.CharField(max_length=32)),
                ('mother_email', models.EmailField(max_length=254)),
                ('mother_phone', models.CharField(max_length=16)),
                ('father_name', models.CharField(max_length=32)),
                ('father_email', models.EmailField(max_length=254)),
                ('father_phone', models.CharField(max_length=16)),
            ],
        ),
    ]
