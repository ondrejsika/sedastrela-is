# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20160222_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_sent', models.BooleanField(default=False)),
                ('offset', models.CharField(max_length=4, choices=[(b'1d', b'1 den'), (b'7d', b'7 dni'), ((b'1m',), b'1 mesic')])),
                ('event', models.ForeignKey(to='event.Event')),
            ],
        ),
    ]
