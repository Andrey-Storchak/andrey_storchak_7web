# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field notes on 'Book'
        m2m_table_name = db.shorten_name(u'pynote_book_notes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'pynote.book'], null=False)),
            ('note', models.ForeignKey(orm[u'pynote.note'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'note_id'])


    def backwards(self, orm):
        # Removing M2M table for field notes on 'Book'
        db.delete_table(db.shorten_name(u'pynote_book_notes'))


    models = {
        u'pynote.book': {
            'Meta': {'object_name': 'Book'},
            'book_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pynote.Note']", 'symmetrical': 'False'})
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