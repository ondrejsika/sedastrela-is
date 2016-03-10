# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_eventnotification'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventnotification',
            unique_together=set([('event', 'offset')]),
        ),
    ]
