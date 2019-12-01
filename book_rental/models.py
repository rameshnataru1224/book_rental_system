# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class BookCategory(models.Model):
    """Class representing a Book category."""
    book_category_name = models.CharField(max_length=150)
    cost = models.FloatField()

    def __str__(self):
        return self.book_category_name


class Book(models.Model):
    """Class representing a Book rented."""
    book_category = models.ForeignKey(BookCategory,
                                      related_name='bookcategory',
                                      on_delete=models.CASCADE,
                                      )
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)

    start_date = models.DateTimeField(_('started at'), auto_now_add=True,
                                      null=False, blank=False)
    end_date = models.DateTimeField(_('ended at'), auto_now_add=True,
                                    null=False, blank=False)

    def __str__(self):
        return self.book_name


class Coustomer(models.Model):
    """Class representing a Coustomer"""
    name = models.CharField(max_length=300, null=True, blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    cost = models.FloatField(default=0)
    book = models.ForeignKey(Book)

    def __str__(self):
        return self.name
