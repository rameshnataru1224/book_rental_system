# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-01 15:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_rental', '0002_book_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cost',
        ),
    ]
