# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20170326_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='paid',
            field=models.BooleanField(default=None),
        ),
    ]
