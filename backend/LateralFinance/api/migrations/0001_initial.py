# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Currency'
        db.create_table('api_currency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('api', ['Currency'])

        # Adding model 'Market'
        db.create_table('api_market', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('api', ['Market'])

        # Adding model 'Company'
        db.create_table('api_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('market', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Market'])),
            ('trading_currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Currency'])),
            ('isin', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('api', ['Company'])

        # Adding model 'Quote'
        db.create_table('api_quote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Company'])),
            ('created_at', self.gf('django.db.models.fields.DateField')()),
            ('open', self.gf('django.db.models.fields.FloatField')()),
            ('high', self.gf('django.db.models.fields.FloatField')()),
            ('close', self.gf('django.db.models.fields.FloatField')()),
            ('low', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('api', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'Currency'
        db.delete_table('api_currency')

        # Deleting model 'Market'
        db.delete_table('api_market')

        # Deleting model 'Company'
        db.delete_table('api_company')

        # Deleting model 'Quote'
        db.delete_table('api_quote')


    models = {
        'api.company': {
            'Meta': {'object_name': 'Company'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isin': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'market': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.Market']"}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'trading_currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.Currency']"})
        },
        'api.currency': {
            'Meta': {'object_name': 'Currency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'api.market': {
            'Meta': {'object_name': 'Market'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'api.quote': {
            'Meta': {'object_name': 'Quote'},
            'close': ('django.db.models.fields.FloatField', [], {}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api.Company']"}),
            'created_at': ('django.db.models.fields.DateField', [], {}),
            'high': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low': ('django.db.models.fields.FloatField', [], {}),
            'open': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['api']