from django import forms
from book_rental.models import BookCategory, Coustomer, Book


class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = '__all__'


class CoustomerForm(forms.ModelForm):
    class Meta:
        model = Coustomer
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('book_category',)

