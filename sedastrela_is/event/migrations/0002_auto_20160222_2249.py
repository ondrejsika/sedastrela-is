# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='person',
            field=models.ForeignKey(default=1, to='person.Person'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='event',
            field=models.ForeignKey(to='event.Event'),
        ),
    ]
