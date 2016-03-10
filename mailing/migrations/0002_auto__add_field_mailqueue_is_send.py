# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MailQueue.is_send'
        db.add_column(u'mailing_mailqueue', 'is_send',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MailQueue.is_send'
        db.delete_column(u'mailing_mailqueue', 'is_send')


    models = {
        u'mailing.mailqueue': {
            'Meta': {'object_name': 'MailQueue'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'email_from': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'email_to': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_html': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_send': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mailing']