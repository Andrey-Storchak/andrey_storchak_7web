from django.conf.urls import patterns, include, url
from django.conf import settings


import views



urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^/add$', views.AddNoteView.as_view(), name='add_note'),
)
