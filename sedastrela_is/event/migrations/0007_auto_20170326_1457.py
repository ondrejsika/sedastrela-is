# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_attendee_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='attendee',
            unique_together=set([('event', 'person')]),
        ),
    ]
