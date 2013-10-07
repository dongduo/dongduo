# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'zhidao_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.UserProfile'])),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('detail', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'zhidao', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'zhidao_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.UserProfile'])),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('detail', self.gf('django.db.models.fields.TextField')()),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['zhidao.Question'])),
        ))
        db.send_create_signal(u'zhidao', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'zhidao_question')

        # Deleting model 'Answer'
        db.delete_table(u'zhidao_answer')


    models = {
        u'comments.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'zhidao.answer': {
            'Meta': {'object_name': 'Answer'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserProfile']"}),
            'detail': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['zhidao.Question']"})
        },
        u'zhidao.question': {
            'Meta': {'object_name': 'Question'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserProfile']"}),
            'detail': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['zhidao']