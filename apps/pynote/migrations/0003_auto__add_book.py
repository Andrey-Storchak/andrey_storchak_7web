# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'pynote_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'pynote', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'pynote_book')


    models = {
        u'pynote.book': {
            'Meta': {'object_name': 'Book'},
            'book_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pynote.note': {
            'Meta': {'object_name': 'Note'},
            'attach': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['pynote']