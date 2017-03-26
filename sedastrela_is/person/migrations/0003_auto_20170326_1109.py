# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20160310_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='father_address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='father_email_preferred',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='father_facebook',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='father_facebook_preferred',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='father_phone_call_preferred',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='father_phone_sms_preferred',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='mother_address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='mother_email_preferred',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='mother_facebook',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='mother_facebook_preferred',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='mother_phone_call_preferred',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='mother_phone_sms_preferred',
            field=models.BooleanField(default=True),
        ),
    ]
