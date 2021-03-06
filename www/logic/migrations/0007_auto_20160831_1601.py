# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-31 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0006_auto_20160821_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeInterested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_uuid', models.CharField(db_index=True, default='00000000000000000000000000000000', max_length=36)),
                ('job_id', models.IntegerField(db_index=True)),
                ('qlm_user_id', models.IntegerField(db_index=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'be_interested',
            },
        ),
        migrations.RenameField(
            model_name='conversation',
            old_name='share_id',
            new_name='be_interested_id',
        ),
        migrations.RenameField(
            model_name='share',
            old_name='from_user_id',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='share',
            name='to_user_id',
        ),
    ]
