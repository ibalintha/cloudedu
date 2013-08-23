#!/usr/bin/env python
# coding: utf-8
# alvin@2013-08-23 19:14:07
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:

from django.conf.urls import patterns, include, url
from views import DataDictList, DataDictCreate, DataDictDelete, DataDictUpdate

urlpatterns = patterns('essential.views',
    url(r'^$', DataDictList.as_view(), name='essential-index'),
    url(r'^add/$', DataDictCreate.as_view(), name='datadict-add'),
    url(r'^(?P<pk>\d+)/$', DataDictUpdate.as_view(), name='datadict-update'),
    url(r'^(?P<pk>\d+)/delete/$', DataDictDelete.as_view(), name='datadict-delete'),
)
