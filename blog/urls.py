from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

URLPatterns = [
    path ('', views.post_list, name='post_list'),
]