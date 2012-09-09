# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Company.isin'
        db.alter_column('api_company', 'isin', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

    def backwards(self, orm):

        # Changing field 'Company.isin'
        db.alter_column('api_company', 'isin', self.gf('django.db.models.fields.CharField')(default='', max_length=20))

    models = {
        'api.company': {
            'Meta': {'object_name': 'Company'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isin': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
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
            'open': ('django.db.models.fields.FloatField', [], {}),
            'volume': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['api']