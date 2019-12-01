# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-30 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='started at')),
                ('end_date', models.DateTimeField(auto_now_add=True, verbose_name='ended at')),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_category_name', models.CharField(max_length=150)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Coustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('address', models.TextField(blank=True, max_length=300, null=True)),
                ('cost', models.FloatField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_rental.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookcategory', to='book_rental.BookCategory'),
        ),
    ]