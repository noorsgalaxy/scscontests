# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-13 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scs_user', '0003_userinfo_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(default='Set Your Username', max_length=100),
        ),
    ]