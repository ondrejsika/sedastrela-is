# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20160310_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventnotification',
            name='channel',
            field=models.CharField(default='email', max_length=5, choices=[(b'email', b'Email'), (b'call', b'Call'), (b'sms', b'SMS')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventnotification',
            name='sent_dt',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eventnotification',
            name='offset',
            field=models.CharField(blank=True, max_length=4, null=True, choices=[(None, b'Ihned'), (b'1d', b'1 den'), (b'7d', b'7 dni'), ((b'1m',), b'1 mesic')]),
        ),
    ]
