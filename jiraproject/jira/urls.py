# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.jira_title, name='jira_title'),
    url(r'(?P<context_id>\d)/$', views.jira_context, name="jira_context"),
]
