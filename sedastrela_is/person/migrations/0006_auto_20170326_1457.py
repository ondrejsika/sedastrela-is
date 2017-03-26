# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_person_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='token',
            field=models.CharField(max_length=32, blank=True),
        ),
    ]
