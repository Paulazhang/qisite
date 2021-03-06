# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'account_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('birthDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('createBy', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='userCreated', null=True, to=orm['account.User'])),
            ('modifyBy', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='userModified', null=True, to=orm['account.User'])),
            ('createTime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 24, 0, 0))),
            ('modifyTime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 24, 0, 0))),
        ))
        db.send_create_signal(u'account', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'account_user')


    models = {
        u'account.user': {
            'Meta': {'ordering': "['name']", 'object_name': 'User'},
            'birthDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'createBy': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'userCreated'", 'null': 'True', 'to': u"orm['account.User']"}),
            'createTime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 24, 0, 0)'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modifyBy': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'userModified'", 'null': 'True', 'to': u"orm['account.User']"}),
            'modifyTime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 24, 0, 0)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['account']