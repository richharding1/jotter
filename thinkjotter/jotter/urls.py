from django.urls import path
from . import views


app_name = 'jotter'

urlpatterns = [
    path("", views.all_entries, name='all_entries'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('category_search/', views.category_search, name='category_search'),
    path('hashtag_search/', views.hashtag_search, name='hashtag_search'),
]