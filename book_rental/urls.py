from django.conf.urls import url
from . import views

app_name = 'book_rental'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createcategoryform/$', views.createcategoryform, name='createcategoryform'),
    url(r'^create_coustomer/$', views.create_coustomer, name='create_coustomer'),
    url(r'^(?P<category_id>[0-9]+)/book_selection/$', views.book_selection, name='book_selection'),
    url(r'^(?P<category_id>[0-9]+)/add_book/', views.add_book, name='add_book'),
]