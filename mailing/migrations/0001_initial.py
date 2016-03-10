# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MailQueue'
        db.create_table(u'mailing_mailqueue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_from', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('email_to', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('is_html', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'mailing', ['MailQueue'])


    def backwards(self, orm):
        # Deleting model 'MailQueue'
        db.delete_table(u'mailing_mailqueue')


    models = {
        u'mailing.mailqueue': {
            'Meta': {'object_name': 'MailQueue'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'email_from': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'email_to': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_html': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mailing']