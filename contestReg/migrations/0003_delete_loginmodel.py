# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 12:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contestReg', '0002_loginmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoginModel',
        ),
    ]
