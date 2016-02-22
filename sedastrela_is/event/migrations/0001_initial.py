# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=4, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('event', models.ForeignKey(to='person.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_dt', models.DateTimeField()),
                ('to_dt', models.DateTimeField()),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
