# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_person_facebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='token',
            field=models.CharField(default='a', max_length=32),
            preserve_default=False,
        ),
    ]
