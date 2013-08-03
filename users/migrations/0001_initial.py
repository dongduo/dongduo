# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'users_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'users', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'users_userprofile')


    models = {
        u'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['users']