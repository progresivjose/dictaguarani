# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Word.language'
        db.add_column(u'words_word', 'language',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=123, related_name='word_language_id', to=orm['languages.Language']),
                      keep_default=False)

        # Adding field 'Word.typeword'
        db.add_column(u'words_word', 'typeword',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=123, related_name='typeword_id', to=orm['typewords.TypeWord']),
                      keep_default=False)

        # Adding M2M table for field translate on 'Word'
        m2m_table_name = db.shorten_name(u'words_word_translate')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_word', models.ForeignKey(orm[u'words.word'], null=False)),
            ('to_word', models.ForeignKey(orm[u'words.word'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_word_id', 'to_word_id'])

        # Adding M2M table for field synonym on 'Word'
        m2m_table_name = db.shorten_name(u'words_word_synonym')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_word', models.ForeignKey(orm[u'words.word'], null=False)),
            ('to_word', models.ForeignKey(orm[u'words.word'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_word_id', 'to_word_id'])


    def backwards(self, orm):
        # Deleting field 'Word.language'
        db.delete_column(u'words_word', 'language_id')

        # Deleting field 'Word.typeword'
        db.delete_column(u'words_word', 'typeword_id')

        # Removing M2M table for field translate on 'Word'
        db.delete_table(db.shorten_name(u'words_word_translate'))

        # Removing M2M table for field synonym on 'Word'
        db.delete_table(db.shorten_name(u'words_word_synonym'))


    models = {
        u'languages.language': {
            'Meta': {'object_name': 'Language'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'typewords.typeword': {
            'Meta': {'object_name': 'TypeWord'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'typeword_language_id'", 'to': u"orm['languages.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'words.word': {
            'Meta': {'object_name': 'Word'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'word_language_id'", 'to': u"orm['languages.Language']"}),
            'synonym': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'synonym_rel_+'", 'to': u"orm['words.Word']"}),
            'translate': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'translate_rel_+'", 'to': u"orm['words.Word']"}),
            'typeword': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'typeword_id'", 'to': u"orm['typewords.TypeWord']"}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['words']