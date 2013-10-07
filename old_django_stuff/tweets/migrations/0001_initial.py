# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tweet'
        db.create_table(u'tweets_tweet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.UserProfile'])),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('detail', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('fwd_tweet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tweets.Tweet'], null=True, on_delete=models.SET_NULL)),
        ))
        db.send_create_signal(u'tweets', ['Tweet'])


    def backwards(self, orm):
        # Deleting model 'Tweet'
        db.delete_table(u'tweets_tweet')


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
        u'tweets.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserProfile']"}),
            'detail': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'fwd_tweet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tweets.Tweet']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['tweets']