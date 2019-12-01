# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from book_rental.models import BookCategory, Book, Coustomer
# Register your models here.

admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(Coustomer)
