# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-05 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scs_user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='contest_attempted',
            new_name='contest_registered',
        ),
    ]
