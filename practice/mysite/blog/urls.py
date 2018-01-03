# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_title, name='blog_title'),
    url(r'(?P<context_id>\d)/$', views.blog_context, name="blog_context"),
]
