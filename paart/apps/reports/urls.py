from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('reports.views',
                       url(r'^$', 'agency_search_report', (), 'agency_search_report'),
                       url(r'^project_complete/$', 'agency_project_completion_report', (),
                           'agency_project_completion_report'),
                       )
