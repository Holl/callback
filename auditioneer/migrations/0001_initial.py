# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Audition'
        db.create_table(u'auditioneer_audition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.IntegerField')()),
            ('longitude', self.gf('django.db.models.fields.IntegerField')()),
            ('location_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('audition_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('production_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts_manager.ProductionProfile'])),
        ))
        db.send_create_signal(u'auditioneer', ['Audition'])

        # Adding M2M table for field actor_user on 'Audition'
        m2m_table_name = db.shorten_name(u'auditioneer_audition_actor_user')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('audition', models.ForeignKey(orm[u'auditioneer.audition'], null=False)),
            ('actorprofile', models.ForeignKey(orm[u'accounts_manager.actorprofile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['audition_id', 'actorprofile_id'])

        # Adding M2M table for field tag on 'Audition'
        m2m_table_name = db.shorten_name(u'auditioneer_audition_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('audition', models.ForeignKey(orm[u'auditioneer.audition'], null=False)),
            ('tag', models.ForeignKey(orm[u'accounts_manager.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['audition_id', 'tag_id'])

        # Adding model 'Part'
        db.create_table(u'auditioneer_part', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('age_range', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('audition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auditioneer.Audition'])),
        ))
        db.send_create_signal(u'auditioneer', ['Part'])


    def backwards(self, orm):
        # Deleting model 'Audition'
        db.delete_table(u'auditioneer_audition')

        # Removing M2M table for field actor_user on 'Audition'
        db.delete_table(db.shorten_name(u'auditioneer_audition_actor_user'))

        # Removing M2M table for field tag on 'Audition'
        db.delete_table(db.shorten_name(u'auditioneer_audition_tag'))

        # Deleting model 'Part'
        db.delete_table(u'auditioneer_part')


    models = {
        u'accounts_manager.actorprofile': {
            'Meta': {'object_name': 'ActorProfile'},
            'age': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'highlight_reel': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounts_manager.Tag']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'actor'", 'unique': 'True', 'to': u"orm['accounts_manager.MainUser']"})
        },
        u'accounts_manager.mainuser': {
            'Meta': {'object_name': 'MainUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'accounts_manager.productionprofile': {
            'Meta': {'object_name': 'ProductionProfile'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'company_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts_manager.MainUser']", 'unique': 'True'})
        },
        u'accounts_manager.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'auditioneer.audition': {
            'Meta': {'object_name': 'Audition'},
            'actor_user': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounts_manager.ActorProfile']", 'null': 'True', 'symmetrical': 'False'}),
            'audition_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.IntegerField', [], {}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'longitude': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'production_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts_manager.ProductionProfile']"}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounts_manager.Tag']", 'symmetrical': 'False'})
        },
        u'auditioneer.part': {
            'Meta': {'object_name': 'Part'},
            'age_range': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'audition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auditioneer.Audition']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['auditioneer']