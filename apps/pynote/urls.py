from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
