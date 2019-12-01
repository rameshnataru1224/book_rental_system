# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, get_object_or_404

from book_rental.models import BookCategory, Book
from django.http import HttpResponseRedirect
from book_rental.forms import BookCategoryForm, BookForm, CoustomerForm


def index(request):
    category_list = BookCategory.objects.all()
    return render(request, 'book_rental/index.html',
                  {'category_list': category_list})


def createcategoryform(request):
    if request.method == "POST":
        form = BookCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('book_rental:index'))
    form = BookCategoryForm()
    return render(request, "book_rental/categoryform.html", {'form': form})


def book_selection(request, category_id):
    bookcategory = get_object_or_404(BookCategory, id=category_id)
    if request.method == 'POST':
        days = request.POST['days']
        if days:
            if days > 2:
                check_values = request.POST.getlist('books[]')
                number_of_books = len(check_values)
                result = number_of_books * 2 * bookcategory.cost * \
                    (int(days) - 2) + number_of_books * bookcategory.cost * 2
                return render(request,
                              'book_rental/calculate.html',
                              {'result': result})
            else:
                check_values = request.POST.getlist('books[]')
                number_of_books = len(check_values)
                result = number_of_books * bookcategory.cost * int(days)
                return render(request,
                              'book_rental/calculate.html',
                              {'result': result})

    books = Book.objects.filter(book_category=bookcategory)
    return render(request, 'book_rental/bookcategory.html',
                  {'bookcategory': bookcategory, 'books': books})


def add_book(request, category_id):
    bookcategory = get_object_or_404(BookCategory, id=category_id)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.book_category = bookcategory
            instance.save()
            return HttpResponseRedirect(
                reverse(
                    'book_rental:book_selection',
                    args=[
                        category_id,
                    ]))
    form = BookForm()
    return render(request, 'book_rental/add_book.html', {'form': form})


def create_coustomer(request):
    if request.method == "POST":
        form = CoustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('book_rental:index'))
    form = CoustomerForm()
    return render(request, "book_rental/customerform.html", {'form': form})
