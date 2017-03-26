# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20170326_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='facebook',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
